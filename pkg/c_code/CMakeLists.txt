cmake_minimum_required(VERSION 3.10)

project(ray_tracing_iid)

set (CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS_RELEASE "-O3")


if(NOT DEFINED C_INTERFACE_INSTALL)
  message(FATAL_ERROR "set install path for c interface: \n cmake -DC_INTERFACE_INSTALL=/my/install/path ../ ")
endif()

find_package (Eigen3 3.3 REQUIRED NO_MODULE)

include_directories ( "${EIGEN3_INCLUDE_DIR}" )

add_library(c_interface SHARED local_tools.cpp)

set_target_properties(c_interface PROPERTIES OUTPUT_NAME "c_interface")
set_target_properties(c_interface PROPERTIES SUFFIX ".so")
set_target_properties(c_interface PROPERTIES PREFIX "")

get_property(_lib_name TARGET c_interface PROPERTY OUTPUT_NAME)
get_property(_lib_suffix TARGET c_interface PROPERTY SUFFIX)

set(lib_filename ${_lib_name}${_lib_suffix})

target_link_libraries(c_interface PUBLIC Eigen3::Eigen)

configure_file(install_path.py.in ${CMAKE_SOURCE_DIR}/install_path.py)

install(TARGETS c_interface DESTINATION ${C_INTERFACE_INSTALL})
