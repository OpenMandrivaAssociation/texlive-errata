Name:		texlive-errata
Version:	42428
Release:	1
Summary:	Error markup for LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/errata
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/errata.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/errata.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/errata.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a simple infrastructure for recording
errata in LaTeX documents. This allows the user to maintain an
updated version of the document (with all errors corrected) and
to automatically generate an errata document highlighting the
difference to the published version.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/errata/errata.sty
%doc %{_texmfdistdir}/doc/latex/errata/README
%doc %{_texmfdistdir}/doc/latex/errata/errata-errata.tex
%doc %{_texmfdistdir}/doc/latex/errata/errata.pdf
#- source
%doc %{_texmfdistdir}/source/latex/errata/errata.dtx
%doc %{_texmfdistdir}/source/latex/errata/errata.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
