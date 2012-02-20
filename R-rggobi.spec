%global packname  rggobi
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.1.17
Release:          1
Summary:          Interface between R and GGobi
Group:            Sciences/Mathematics
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-RGtk2 R-utils R-methods 
Requires:         R-reshape 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-RGtk2 R-utils R-methods 
BuildRequires:    R-reshape 
BuildRequires:    ggobi
BuildRequires:    ggobi-devel
BuildRequires:    octave-devel
Patch0:           rggobi_2.1.17-format.patch

%description
The rggobi package provides a command-line interface to GGobi, an
interactive and dynamic graphics package. Rggobi complements GGobi's
graphical user interface, providing a way to fluidly transition between
analysis and exploration, as well as automating common tasks.

%prep
%setup -q -c -n %{packname}
%patch0 -p1

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
if [ x$DISPLAY != x ];	then %{_bindir}/R CMD check %{packname}
else			true
fi

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
