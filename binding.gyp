{
  "targets": [{
    "target_name": "leveldown",
    "conditions": [
      ["OS == 'win'", {
        "defines": [
          "_HAS_EXCEPTIONS=0"
        ],
        "msvs_settings": {
          "VCCLCompilerTool": {
            "RuntimeTypeInfo": "false",
            "EnableFunctionLevelLinking": "true",
            "ExceptionHandling": "2",
            "DisableSpecificWarnings": [ "4355", "4530" ,"4267", "4244", "4506" ]
          }
        }
      }],
      ["OS == 'linux'", {
        "cflags": [],
        "cflags!": [ "-fno-tree-vrp"]
      }],
      ["OS == 'android'", {
        "cflags": [ "-fPIC" ],
        "ldflags": [ "-fPIC" ],
        "cflags!": [
          "-fno-tree-vrp",
          "-fno-exceptions",
          "-mfloat-abi=hard",
          "-fPIE"
        ],
        "cflags_cc!": [ "-fno-exceptions" ],
        "ldflags!": [ "-fPIE" ],
        "libraries": [
          "-L$(NODE_LIB_DIR)",
          "-lnode" # Link to libnode.so as a workaround to https://github.com/android-ndk/ndk/issues/201#issuecomment-248060092
        ]
      }],
      ["target_arch == 'arm'", {
        "cflags": [ "-mfloat-abi=hard" ]
      }]
    ],
    "dependencies": [
      "<(module_root_dir)/deps/leveldb/leveldb.gyp:leveldb"
    ],
    "include_dirs"  : [
      "<!(node -e \"require('napi-macros')\")"
    ],
    "sources": [
      "binding.cc"
    ]
  }]
}
