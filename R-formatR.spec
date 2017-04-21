#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-formatR
Version  : 1.4
Release  : 26
URL      : http://cran.r-project.org/src/contrib/formatR_1.4.tar.gz
Source0  : http://cran.r-project.org/src/contrib/formatR_1.4.tar.gz
Summary  : Format R Code Automatically
Group    : Development/Tools
License  : MIT
BuildRequires : R-knitr
BuildRequires : clr-R-helpers

%description
# formatR
[![Build Status](https://travis-ci.org/yihui/formatR.svg)](https://travis-ci.org/yihui/formatR)

%prep
%setup -q -c -n formatR

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484537390

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1484537390
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library formatR
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library formatR


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/formatR/DESCRIPTION
/usr/lib64/R/library/formatR/INDEX
/usr/lib64/R/library/formatR/Meta/Rd.rds
/usr/lib64/R/library/formatR/Meta/hsearch.rds
/usr/lib64/R/library/formatR/Meta/links.rds
/usr/lib64/R/library/formatR/Meta/nsInfo.rds
/usr/lib64/R/library/formatR/Meta/package.rds
/usr/lib64/R/library/formatR/Meta/vignette.rds
/usr/lib64/R/library/formatR/NAMESPACE
/usr/lib64/R/library/formatR/NEWS
/usr/lib64/R/library/formatR/R/formatR
/usr/lib64/R/library/formatR/R/formatR.rdb
/usr/lib64/R/library/formatR/R/formatR.rdx
/usr/lib64/R/library/formatR/doc/formatR.R
/usr/lib64/R/library/formatR/doc/formatR.Rmd
/usr/lib64/R/library/formatR/doc/formatR.html
/usr/lib64/R/library/formatR/doc/index.html
/usr/lib64/R/library/formatR/format/messy.R
/usr/lib64/R/library/formatR/help/AnIndex
/usr/lib64/R/library/formatR/help/aliases.rds
/usr/lib64/R/library/formatR/help/formatR.rdb
/usr/lib64/R/library/formatR/help/formatR.rdx
/usr/lib64/R/library/formatR/help/paths.rds
/usr/lib64/R/library/formatR/html/00Index.html
/usr/lib64/R/library/formatR/html/R.css
/usr/lib64/R/library/formatR/shiny/DESCRIPTION
/usr/lib64/R/library/formatR/shiny/Readme.md
/usr/lib64/R/library/formatR/shiny/server.R
/usr/lib64/R/library/formatR/shiny/ui.R
/usr/lib64/R/library/formatR/shiny/www/shiny-handler.js
