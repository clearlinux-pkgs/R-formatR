#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-formatR
Version  : 1.13
Release  : 91
URL      : https://cran.r-project.org/src/contrib/formatR_1.13.tar.gz
Source0  : https://cran.r-project.org/src/contrib/formatR_1.13.tar.gz
Summary  : Format R Code Automatically
Group    : Development/Tools
License  : MIT
BuildRequires : R-knitr
BuildRequires : buildreq-R

%description
and indent will be added to the code automatically, and comments will be
    preserved under certain conditions, so that R code will be more
    human-readable and tidy. There is also a Shiny app as a user interface in
    this package (see tidy_app()).

%prep
%setup -q -n formatR
cd %{_builddir}/formatR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671728015

%install
export SOURCE_DATE_EPOCH=1671728015
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/formatR/NEWS.Rd
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
