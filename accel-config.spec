#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : accel-config
Version  : accel.config.v3.5.2
Release  : 1
URL      : https://github.com/intel/idxd-config/archive/refs/tags/accel-config-v3.5.2.tar.gz
Source0  : https://github.com/intel/idxd-config/archive/refs/tags/accel-config-v3.5.2.tar.gz
Summary  : Configure accfg subsystem devices
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.1 MIT
Requires: accel-config-bin = %{version}-%{release}
Requires: accel-config-lib = %{version}-%{release}
Requires: accel-config-license = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : buildreq-configure
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(uuid)
BuildRequires : sed
BuildRequires : xmlto
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# accel-config
Utility library for controlling and configuring DSA (Data-Streaming Accelerator)
sub-system in the Linux kernel

%package bin
Summary: bin components for the accel-config package.
Group: Binaries
Requires: accel-config-license = %{version}-%{release}

%description bin
bin components for the accel-config package.


%package dev
Summary: dev components for the accel-config package.
Group: Development
Requires: accel-config-lib = %{version}-%{release}
Requires: accel-config-bin = %{version}-%{release}
Provides: accel-config-devel = %{version}-%{release}
Requires: accel-config = %{version}-%{release}

%description dev
dev components for the accel-config package.


%package lib
Summary: lib components for the accel-config package.
Group: Libraries
Requires: accel-config-license = %{version}-%{release}

%description lib
lib components for the accel-config package.


%package license
Summary: license components for the accel-config package.
Group: Default

%description license
license components for the accel-config package.


%prep
%setup -q -n idxd-config-accel-config-v3.5.2
cd %{_builddir}/idxd-config-accel-config-v3.5.2

%build
## build_prepend content
bash autogen.sh
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673029125
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static --disable-docs
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1673029125
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/accel-config
cp %{_builddir}/idxd-config-accel-config-v3.5.2/Documentation/COPYING %{buildroot}/usr/share/package-licenses/accel-config/cac5aabfbd6b7df58097e0f2efc0021152a31247 || :
cp %{_builddir}/idxd-config-accel-config-v3.5.2/Documentation/copyright.txt %{buildroot}/usr/share/package-licenses/accel-config/286b18774f60cb7349670ad94a0614927f9a83e2 || :
cp %{_builddir}/idxd-config-accel-config-v3.5.2/LICENSE_GPL_2_0 %{buildroot}/usr/share/package-licenses/accel-config/216629914867066060ebd55c489c17839d566b02 || :
cp %{_builddir}/idxd-config-accel-config-v3.5.2/accfg/lib/LICENSE_LGPL_2_1 %{buildroot}/usr/share/package-licenses/accel-config/b6bf700828e326ac460dadc88c246f9ee43a29d4 || :
cp %{_builddir}/idxd-config-accel-config-v3.5.2/ccan/array_size/LICENSE %{buildroot}/usr/share/package-licenses/accel-config/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/idxd-config-accel-config-v3.5.2/ccan/build_assert/LICENSE %{buildroot}/usr/share/package-licenses/accel-config/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/idxd-config-accel-config-v3.5.2/ccan/check_type/LICENSE %{buildroot}/usr/share/package-licenses/accel-config/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/idxd-config-accel-config-v3.5.2/ccan/container_of/LICENSE %{buildroot}/usr/share/package-licenses/accel-config/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/idxd-config-accel-config-v3.5.2/ccan/endian/LICENSE %{buildroot}/usr/share/package-licenses/accel-config/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/idxd-config-accel-config-v3.5.2/ccan/list/LICENSE %{buildroot}/usr/share/package-licenses/accel-config/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305 || :
cp %{_builddir}/idxd-config-accel-config-v3.5.2/ccan/minmax/LICENSE %{buildroot}/usr/share/package-licenses/accel-config/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/idxd-config-accel-config-v3.5.2/ccan/short_types/LICENSE %{buildroot}/usr/share/package-licenses/accel-config/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/idxd-config-accel-config-v3.5.2/ccan/str/LICENSE %{buildroot}/usr/share/package-licenses/accel-config/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/idxd-config-accel-config-v3.5.2/debian/copyright %{buildroot}/usr/share/package-licenses/accel-config/0bc0d2aab4a02c5a504ddd86cd5c8722793689f2 || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/accel-config

%files dev
%defattr(-,root,root,-)
/usr/include/accel-config/libaccel_config.h
/usr/lib64/libaccel-config.so
/usr/lib64/pkgconfig/libaccel-config.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libaccel-config.so.1
/usr/lib64/libaccel-config.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/accel-config/0bc0d2aab4a02c5a504ddd86cd5c8722793689f2
/usr/share/package-licenses/accel-config/216629914867066060ebd55c489c17839d566b02
/usr/share/package-licenses/accel-config/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305
/usr/share/package-licenses/accel-config/286b18774f60cb7349670ad94a0614927f9a83e2
/usr/share/package-licenses/accel-config/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
/usr/share/package-licenses/accel-config/b6bf700828e326ac460dadc88c246f9ee43a29d4
/usr/share/package-licenses/accel-config/cac5aabfbd6b7df58097e0f2efc0021152a31247
