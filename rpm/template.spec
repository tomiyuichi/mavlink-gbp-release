Name:           ros-lunar-mavlink
Version:        2017.5.25
Release:        1%{?dist}
Summary:        ROS mavlink package

Group:          Development/Libraries
License:        LGPLv3
URL:            http://qgroundcontrol.org/mavlink/
Source0:        %{name}-%{version}.tar.gz

Requires:       python-devel
Requires:       ros-lunar-catkin
BuildRequires:  cmake
BuildRequires:  python-devel
BuildRequires:  python-future
BuildRequires:  python-lxml
BuildRequires:  python-setuptools

%description
MAVLink message marshaling library. This package provides C-headers and C++11
library for both 1.0 and 2.0 versions of protocol. For pymavlink use separate
install via rosdep (python-pymavlink).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Thu May 25 2017 Vladimir Ermakov <vooon341@gmail.com> - 2017.5.25-1
- Autogenerated by Bloom

* Thu May 25 2017 Vladimir Ermakov <vooon341@gmail.com> - 2017.5.25-0
- Autogenerated by Bloom

