// Runs an o2i loom GGUF: one line of text per stdin line, IPA per stdout line.
#include "loom/loom.h"

#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

static std::vector<double> utf8_to_codepoints(const std::string& s) {
    std::vector<double> out;
    for (size_t i = 0; i < s.size();) {
        const unsigned char c = s[i];
        const int len = c < 0x80 ? 1 : c < 0xE0 ? 2 : c < 0xF0 ? 3 : 4;
        uint32_t cp = len == 1 ? c : c & (0xFF >> (len + 1));
        for (int k = 1; k < len; ++k) cp = (cp << 6) | (s[i + k] & 0x3F);
        out.push_back(cp);
        i += len;
    }
    return out;
}

static std::string codepoints_to_utf8(const std::vector<double>& cps) {
    std::string out;
    for (double d : cps) {
        const auto cp = static_cast<uint32_t>(d);
        if (cp < 0x80) {
            out += char(cp);
        } else if (cp < 0x800) {
            out += char(0xC0 | (cp >> 6)); out += char(0x80 | (cp & 0x3F));
        } else if (cp < 0x10000) {
            out += char(0xE0 | (cp >> 12)); out += char(0x80 | ((cp >> 6) & 0x3F)); out += char(0x80 | (cp & 0x3F));
        } else {
            out += char(0xF0 | (cp >> 18)); out += char(0x80 | ((cp >> 12) & 0x3F));
            out += char(0x80 | ((cp >> 6) & 0x3F)); out += char(0x80 | (cp & 0x3F));
        }
    }
    return out;
}

int main(int argc, char** argv) {
    if (argc < 2) {
        std::fprintf(stderr, "usage: o2i_loom MODEL.gguf [LANG_INDEX] < lines\n");
        return 2;
    }
    const double lang = argc > 2 ? std::stod(argv[2]) : 0.0;
    loom::Device device = loom::Device::open("cpu", 0);
    const loom::Backends backends = device.backends();
    auto model = loom::GgufModel::load(argv[1], backends);
    loom::Session session(*model, backends);
    std::string line;
    while (std::getline(std::cin, line)) {
        std::unordered_map<std::string, loom::LoomLuaBridge::Value> inputs;
        inputs["text"] = utf8_to_codepoints(line);
        inputs["lang"] = lang;
        const auto result = session.bridge().call("infer", inputs);
        const auto* cps = std::get_if<std::vector<double>>(&result);
        std::puts(cps ? codepoints_to_utf8(*cps).c_str() : "");
    }
    return 0;
}
