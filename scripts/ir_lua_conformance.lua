-- Check interpreter.lua against IR conformance vector files (section 8.4).
--
--   luajit scripts/ir_lua_conformance.lua tests/conformance/ir-v1/*.jsonl
--
-- For each file it prints N in, N pass and every failed case, then a total.
-- The exit status is 1 when a case fails.
local here = (arg[0]:match("^(.*)/[^/]*$") or ".")
package.path = here .. "/../orthography2ipa/ir/?.lua;" .. package.path
local M = require("interpreter")

local function same(a, b)
  if #a ~= #b then return false end
  for i = 1, #a do if a[i] ~= b[i] then return false end end
  return true
end

local function cps(t) return table.concat(t, " ") end

local total, passed = 0, 0
for i = 1, #arg do
  local f = assert(io.open(arg[i], "rb"))
  local it, err
  local n, ok = 0, 0
  for line in f:lines() do
    local rec = M.json_decode(line)
    if rec.kind == "ir" then
      local good, res = pcall(M.new, rec.ir)
      if good then it, err = res, nil else it, err = nil, tostring(res) end
    else
      n = n + 1
      local good, res
      if it then good, res = pcall(it.transcribe_cps, it, rec.input, 1) else good, res = false, err end
      local pass
      if rec.expect_error then
        pass = not good and string.find(tostring(res), rec.expect_error, 1, true) ~= nil
      else
        pass = good and same(res, rec.expect)
      end
      if pass then
        ok = ok + 1
      else
        io.write(("  FAIL %s case %d: input [%s] got %s\n"):format(arg[i], n, cps(rec.input),
          good and ("[" .. cps(res) .. "]") or ("error " .. tostring(res))))
      end
    end
  end
  f:close()
  io.write(("%s: N in %d, N pass %d, N fail %d\n"):format(arg[i], n, ok, n - ok))
  total, passed = total + n, passed + ok
end
io.write(("total: files %d, N in %d, N pass %d, N fail %d\n"):format(#arg, total, passed, total - passed))
os.exit(passed == total and 0 or 1)
