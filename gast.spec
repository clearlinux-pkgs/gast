#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7B24DA8C9551659F (sguelton@quarkslab.com)
#
Name     : gast
Version  : 0.2.0
Release  : 4
URL      : https://pypi.python.org/packages/5c/78/ff794fcae2ce8aa6323e789d1f8b3b7765f601e7702726f430e814822b96/gast-0.2.0.tar.gz
Source0  : https://pypi.python.org/packages/5c/78/ff794fcae2ce8aa6323e789d1f8b3b7765f601e7702726f430e814822b96/gast-0.2.0.tar.gz
Source99 : https://pypi.python.org/packages/5c/78/ff794fcae2ce8aa6323e789d1f8b3b7765f601e7702726f430e814822b96/gast-0.2.0.tar.gz.asc
Summary  : Python AST that abstracts the underlying Python version
Group    : Development/Tools
License  : BSD-3-Clause
Requires: gast-python3
Requires: gast-python
Requires: astunparse
BuildRequires : astunparse
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
A generic AST to represent Python2 and Python3's Abstract Syntax Tree(AST).
        
        GAST provides a compatibility layer between the AST of various Python versions,
        as produced by ``ast.parse`` from the standard ``ast`` module.

%package python
Summary: python components for the gast package.
Group: Default
Requires: gast-python3

%description python
python components for the gast package.


%package python3
Summary: python3 components for the gast package.
Group: Default
Requires: python3-core

%description python3
python3 components for the gast package.


%prep
%setup -q -n gast-0.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522437492
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
