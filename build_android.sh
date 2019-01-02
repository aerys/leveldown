#!/bin/bash

set -x

for i in "$@"
do
case $i in
    --node-lib-dir=*)
    NODE_LIB_DIR="${i#*=}"
    shift
    ;;
    *)
    # unknown option
    ;;
esac
done

[[ -z $NODE_LIB_DIR ]] && {
    echo "Path to libnode.so must be provided via '--node-lib-dir=<path>' option." > /dev/stderr
    exit 1
}

[[ -n ${ANDROID_HOME} ]] || {
    echo "Missing ANDROID_HOME environment variable." > /dev/stderr
    exit 1
}

npm install

ARCH=arm
DEST_CPU="$ARCH"
SUFFIX="$ARCH-linux-androideabi"
TOOLCHAIN_NAME="$SUFFIX"

if [ ! -d ${ANDROID_HOME}/toolchains/default ]; then
    echo "A standalone toolchain must be installed in ${ANDROID_HOME}/toolchains/default."
    echo "Example: make_standalone_toolchain.py --api 26 --install-dir ${ANDROID_NDK}/toolchains/default --arch arm --force"
    echo "https://developer.android.com/ndk/guides/standalone_toolchain"
    exit 1
fi

export TOOLCHAIN=${ANDROID_HOME}/toolchains/default
export PATH=${TOOLCHAIN}/bin:${PATH}
export AR=${TOOLCHAIN}/bin/${SUFFIX}-ar
export CC=${TOOLCHAIN}/bin/${SUFFIX}-clang
export CXX=${TOOLCHAIN}/bin/${SUFFIX}-clang++
export LINK=${TOOLCHAIN}/bin/${SUFFIX}-clang++

export TARGET_OS=OS_ANDROID_CROSSCOMPILE

GYP_DEFINES="target_arch=$ARCH"
GYP_DEFINES+=" v8_target_arch=$ARCH"
GYP_DEFINES+=" android_target_arch=$ARCH"
GYP_DEFINES+=" host_os=linux OS=android"
export GYP_DEFINES

export NODE_LIB_DIR

node-gyp clean
node-gyp configure --verbose --arch=arm
node-gyp build --verbose
