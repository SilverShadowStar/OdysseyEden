
include(${CMAKE_CURRENT_LIST_DIR}/check-common.cmake)

check(test_version_greater_1 "0")
check(test_version_greater_2 "1")
check(test_version_less_1 "0")
check(test_version_less_2 "1")
check(test_version_equal_1 "0")
check(test_version_equal_2 "1")

if(config AND NOT config STREQUAL NoConfig)
  if(NOT "${test_imported_includes}" MATCHES "^[^;]*/imported[12]/include/with space$")
    message(SEND_ERROR "test_imported_includes is not correct: ${test_imported_includes}")
  endif()
else()
  if(NOT "${test_imported_includes}" MATCHES "^$")
    message(SEND_ERROR "test_imported_includes is not an empty list: ${test_imported_includes}")
  endif()
endif()

check(test_imported_fallback "1")
check(test_imported_fallback2 "1")
check(test_imported_fallback_genex "1")

check(test_alias_file_exe "1")
check(test_alias_file_lib "1")
check(test_alias_target_name "1")
check(test_early_termination_1 "$<:")
check(test_early_termination_2 "$<:,")
check(test_platform_id "${system_name}")
foreach(system Linux Windows Darwin)
  if(system_name STREQUAL system)
    check(test_platform_id_supported 1)
    check(test_platform_id_${system} 1)
    set(platform_supported 1)
  else()
    check(test_platform_id_${system} 0)
  endif()
endforeach()
if(NOT platform_supported)
  check(test_platform_id_supported 0)
endif()
check(lower_case "mi,xed")
check(upper_case "MIX,ED")
check(make_c_identifier "_4f_oo__bar__")
check(equal1 "0")
check(equal2 "1")
check(equal3 "1")
check(equal4 "0")
check(equal5 "1")
check(equal6 "1")
check(equal7 "1")
check(equal8 "1")
check(equal9 "0")
check(equal10 "1")
check(equal11 "1")
check(equal12 "1")
check(equal13 "1")
check(equal14 "1")
check(equal15 "1")
check(equal16 "1")
check(equal17 "0")
check(equal18 "1")
check(equal19 "0")
check(equal20 "1")
check(equal21 "1")
check(equal22 "0")
check(equal23 "1")