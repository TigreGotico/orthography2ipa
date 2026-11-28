local here = arg[0]:match("^(.*)/[^/]*$") or "."
local M = dofile(here .. "/../orthography2ipa/ir/interpreter.lua")
local concat = table.concat

-- luajit scripts/ir_lua_cli.lua IR.json [width]. Each stdin line holds the
-- decimal codepoints of one text; each stdout line holds those of its IPA,
-- or "E " and an error message. A wall-clock line goes to stderr.
local function main(path, width)
  local f = assert(io.open(path, "rb"))
  local text = f:read("*a")
  f:close()
  local ok, it = pcall(M.new, M.json_decode(text))
  if not ok then
    io.stdout:write("E ", tostring(it):gsub("\n", " "), "\n")
    return
  end
  width = tonumber(width) or 1
  local out = {}
  local n = 0
  local t0 = os.clock()
  for line in io.stdin:lines() do
    local cps = {}
    for d in line:gmatch("%d+") do cps[#cps + 1] = tonumber(d) end
    local good, res = pcall(it.transcribe_cps, it, cps, width)
    if good then
      out[#out + 1] = concat(res, " ")
    else
      out[#out + 1] = "E " .. tostring(res):gsub("\n", " ")
    end
    n = n + 1
  end
  local dt = os.clock() - t0
  io.stdout:write(concat(out, "\n"), n > 0 and "\n" or "")
  io.stderr:write(("lua: %d texts in %.3f s cpu\n"):format(n, dt))
end

main(arg[1], arg[2])
