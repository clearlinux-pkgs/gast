#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7B24DA8C9551659F (sguelton@quarkslab.com)
#
Name     : gast
Version  : 0.5.2
Release  : 39
URL      : https://files.pythonhosted.org/packages/53/88/e12484298c9c913b68c1de191fa673f8a976036d98efbdcb60014f14c65c/gast-0.5.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/53/88/e12484298c9c913b68c1de191fa673f8a976036d98efbdcb60014f14c65c/gast-0.5.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/53/88/e12484298c9c913b68c1de191fa673f8a976036d98efbdcb60014f14c65c/gast-0.5.2.tar.gz.asc
Summary  : Python AST that abstracts the underlying Python version
Group    : Development/Tools
License  : BSD-3-Clause
Requires: gast-license = %{version}-%{release}
Requires: gast-python = %{version}-%{release}
Requires: gast-python3 = %{version}-%{release}
Requires: astunparse
BuildRequires : astunparse
BuildRequires : buildreq-distutils3

%description
A generic AST to represent Python2 and Python3's Abstract Syntax Tree(AST).
        
        GAST provides a compatibility layer between the AST of various Python versions,
        as produced by ``ast.parse`` from the standard ``ast`` module.

%package license
Summary: license components for the gast package.
Group: Default

%description license
license components for the gast package.


%package python
Summary: python components for the gast package.
Group: Default
Requires: gast-python3 = %{version}-%{release}

%description python
python components for the gast package.


%package python3
Summary: python3 components for the gast package.
Group: Default
Requires: python3-core
Provides: pypi(gast)

%description python3
python3 components for the gast package.


%prep
%setup -q -n gast-0.5.2
cd %{_builddir}/gast-0.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1627924322
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gast
cp %{_builddir}/gast-0.5.2/LICENSE %{buildroot}/usr/share/package-licenses/gast/a7b1672edaab167e0083c4c26c737daa5755efd8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gast/a7b1672edaab167e0083c4c26c737daa5755efd8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
