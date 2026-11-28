// Runs an o2i loom GGUF: one line of text per stdin line, IPA per stdout line.
// An error goes to stderr, and the exit code is 1.
#include "loom/loom.h"

#include <cstdio>
#include <exception>
#include <iostream>
#include <string>

int main(int argc, char** argv) {
    if (argc < 2) {
        std::fprintf(stderr, "usage: o2i_loom MODEL.gguf [LANG_INDEX] < lines\n");
        return 2;
    }
    const int lang = argc > 2 ? std::stoi(argv[2]) : 0;
    try {
        auto model = loom::GgufModel::load_metadata(argv[1]);
        auto phonemizer = loom::RuleBasedPhonemizer::load(*model);
        if (!phonemizer) {
            std::fprintf(stderr, "%s has no loom.phonemizer.kind\n", argv[1]);
            return 1;
        }
        std::string line;
        while (std::getline(std::cin, line)) {
            std::puts(phonemizer->phonemize(line, lang).ipa.c_str());
        }
    } catch (const std::exception& error) {
        std::fprintf(stderr, "%s\n", error.what());
        return 1;
    }
    return 0;
}
