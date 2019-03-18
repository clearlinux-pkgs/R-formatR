#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-formatR
Version  : 1.6
Release  : 56
URL      : https://cran.r-project.org/src/contrib/formatR_1.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/formatR_1.6.tar.gz
Summary  : Format R Code Automatically
Group    : Development/Tools
License  : MIT
Requires: R-markdown
BuildRequires : R-knitr
BuildRequires : R-markdown
BuildRequires : buildreq-R

%description
This app uses a `textarea` input to store R code, which is reformatted by
`formatR::tidy_source()`. The result is written back in the text box. Click the
`demo` button to load a demo, or paste your own R code here to see what this app
can do.

%prep
%setup -q -c -n formatR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552770866

%install
export SOURCE_DATE_EPOCH=1552770866
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library formatR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library formatR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library formatR
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  formatR || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/formatR/DESCRIPTION
/usr/lib64/R/library/formatR/INDEX
/usr/lib64/R/library/formatR/Meta/Rd.rds
/usr/lib64/R/library/formatR/Meta/features.rds
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
/usr/lib64/R/library/formatR/tests/test-all.R
/usr/lib64/R/library/formatR/tests/testit/test-tidy.R
/usr/lib64/R/library/formatR/tests/testit/test-usage.R
/usr/lib64/R/library/formatR/tests/testit/test-utils.R
