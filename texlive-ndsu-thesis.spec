Name:		texlive-ndsu-thesis
Version:	46639
Release:	2
Summary:	North Dakota State University disquisition class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ndsu-thesis
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ndsu-thesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ndsu-thesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A class for generating disquisitions, intended to be in
compliance with North Dakota State University requirements.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ndsu-thesis
%doc %{_texmfdistdir}/doc/latex/ndsu-thesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
