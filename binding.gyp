{
    "targets": [{
      "target_name": "leveldown"
    , "conditions": [
          ["OS == 'win'", {
              "defines": [
                  "_HAS_EXCEPTIONS=0"
              ]
            , "msvs_settings": {
                  "VCCLCompilerTool": {
                      "RuntimeTypeInfo": "false"
                    , "EnableFunctionLevelLinking": "true"
                    , "ExceptionHandling": "2"
                    , "DisableSpecificWarnings": [ "4355", "4530" ,"4267", "4244", "4506" ]
                  }
              }
          }]
        , ['OS == "linux"', {
              'cflags': [
              ]
            , 'cflags!': [ '-fno-tree-vrp' ]
          }]
        , ['OS == "android"', {
              "cflags": [
                  "-fPIC"
              ]
            , "cflags!": [
                  "-fPIE"
              ]
            , "ldflags": [
                  "-fPIC"
              ]
            , "ldflags!": [
                  "-fPIE"
                , "-pie"
              ]
            , "libraries": [
                  "-L$(NODE_LIB_DIR)"
                , "-lnode" # Link to libnode.so as a workaround to https://github.com/android-ndk/ndk/issues/201#issuecomment-248060092
              ]
          }]
        ]
      , "dependencies": [
            "<(module_root_dir)/deps/leveldb/leveldb.gyp:leveldb"
        ]
      , "include_dirs"  : [
            "<!(node -e \"require('nan')\")"
        ]
      , "sources": [
            "src/batch.cc"
          , "src/batch_async.cc"
          , "src/database.cc"
          , "src/database_async.cc"
          , "src/iterator.cc"
          , "src/iterator_async.cc"
          , "src/leveldown.cc"
          , "src/leveldown_async.cc"
        ]
    }]
}
