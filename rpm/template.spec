Name:           ros-indigo-robot-localization
Version:        2.1.6
Release:        0%{?dist}
Summary:        ROS robot_localization package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/robot_localization
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-indigo-cmake-modules
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-filters
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-tf
BuildRequires:  eigen3-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-gps-common
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf

%description
The robot_localization package provides nonlinear state estimation through
sensor fusion of an abritrary number of sensors.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Nov 06 2014 Tom Moore <tmoore@cra.com> - 2.1.6-0
- Autogenerated by Bloom

* Mon Oct 06 2014 Tom Moore <tmoore@cra.com> - 2.1.5-0
- Autogenerated by Bloom

* Thu Aug 21 2014 Tom Moore <tmoore@cra.com> - 2.1.4-0
- Autogenerated by Bloom

