Name:		texlive-errata
Version:	v0.3
Release:	1
Summary:	Error markup for LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/errata
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/errata.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/errata.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/errata.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package provides a simple infrastructure for recording
errata in LaTeX documents. This allows the user to maintain an
updated version of the document (with all errors corrected) and
to automatically generate an errata document highlighting the
difference to the published version.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
