# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.27

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /workspaces/OdysseyEden/cmake-3.27.0/Bootstrap.cmk/cmake

# The command to remove a file.
RM = /workspaces/OdysseyEden/cmake-3.27.0/Bootstrap.cmk/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /workspaces/OdysseyEden/cmake-3.27.0

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /workspaces/OdysseyEden/cmake-3.27.0

# Include any dependencies generated for this target.
include Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/compiler_depend.make

# Include the progress variables for this target.
include Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/progress.make

# Include the compile flags for this target's objects.
include Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/flags.make

Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/ret1.cxx.o: Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/flags.make
Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/ret1.cxx.o: Tests/CMakeLib/PseudoMemcheck/ret1.cxx
Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/ret1.cxx.o: Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/workspaces/OdysseyEden/cmake-3.27.0/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/ret1.cxx.o"
	cd /workspaces/OdysseyEden/cmake-3.27.0/Tests/CMakeLib/PseudoMemcheck && /usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/ret1.cxx.o -MF CMakeFiles/memcheck_fail.dir/ret1.cxx.o.d -o CMakeFiles/memcheck_fail.dir/ret1.cxx.o -c /workspaces/OdysseyEden/cmake-3.27.0/Tests/CMakeLib/PseudoMemcheck/ret1.cxx

Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/ret1.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/memcheck_fail.dir/ret1.cxx.i"
	cd /workspaces/OdysseyEden/cmake-3.27.0/Tests/CMakeLib/PseudoMemcheck && /usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /workspaces/OdysseyEden/cmake-3.27.0/Tests/CMakeLib/PseudoMemcheck/ret1.cxx > CMakeFiles/memcheck_fail.dir/ret1.cxx.i

Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/ret1.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/memcheck_fail.dir/ret1.cxx.s"
	cd /workspaces/OdysseyEden/cmake-3.27.0/Tests/CMakeLib/PseudoMemcheck && /usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /workspaces/OdysseyEden/cmake-3.27.0/Tests/CMakeLib/PseudoMemcheck/ret1.cxx -o CMakeFiles/memcheck_fail.dir/ret1.cxx.s

# Object files for target memcheck_fail
memcheck_fail_OBJECTS = \
"CMakeFiles/memcheck_fail.dir/ret1.cxx.o"

# External object files for target memcheck_fail
memcheck_fail_EXTERNAL_OBJECTS =

Tests/CMakeLib/PseudoMemcheck/memcheck_fail: Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/ret1.cxx.o
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/build.make
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: Source/libCMakeLib.a
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: Utilities/std/libcmstd.a
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: Source/kwsys/libcmsys.a
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: Utilities/cmcurl/lib/libcmcurl.a
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: Utilities/cmnghttp2/libcmnghttp2.a
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: Utilities/cmexpat/libcmexpat.a
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: Utilities/cmlibarchive/libarchive/libcmlibarchive.a
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: /usr/lib/x86_64-linux-gnu/libssl.so
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: /usr/lib/x86_64-linux-gnu/libcrypto.so
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: Utilities/cmbzip2/libcmbzip2.a
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: Utilities/cmliblzma/libcmliblzma.a
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: Utilities/cmzstd/libcmzstd.a
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: Utilities/cmlibrhash/libcmlibrhash.a
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: Utilities/cmlibuv/libcmlibuv.a
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: Utilities/cmzlib/libcmzlib.a
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: Utilities/cmcppdap/libcmcppdap.a
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: Utilities/cmjsoncpp/libcmjsoncpp.a
Tests/CMakeLib/PseudoMemcheck/memcheck_fail: Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/workspaces/OdysseyEden/cmake-3.27.0/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable memcheck_fail"
	cd /workspaces/OdysseyEden/cmake-3.27.0/Tests/CMakeLib/PseudoMemcheck && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/memcheck_fail.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/build: Tests/CMakeLib/PseudoMemcheck/memcheck_fail
.PHONY : Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/build

Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/clean:
	cd /workspaces/OdysseyEden/cmake-3.27.0/Tests/CMakeLib/PseudoMemcheck && $(CMAKE_COMMAND) -P CMakeFiles/memcheck_fail.dir/cmake_clean.cmake
.PHONY : Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/clean

Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/depend:
	cd /workspaces/OdysseyEden/cmake-3.27.0 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /workspaces/OdysseyEden/cmake-3.27.0 /workspaces/OdysseyEden/cmake-3.27.0/Tests/CMakeLib/PseudoMemcheck /workspaces/OdysseyEden/cmake-3.27.0 /workspaces/OdysseyEden/cmake-3.27.0/Tests/CMakeLib/PseudoMemcheck /workspaces/OdysseyEden/cmake-3.27.0/Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/depend

