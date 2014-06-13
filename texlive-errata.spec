# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/errata
# catalog-date 2008-08-19 20:15:24 +0200
# catalog-license lppl
# catalog-version v0.3
Name:		texlive-errata
Version:	v0.3
Release:	7
Summary:	Error markup for LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/errata
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/errata.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/errata.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/errata.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v0.3-2
+ Revision: 751557
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v0.3-1
+ Revision: 718361
- texlive-errata
- texlive-errata
- texlive-errata
- texlive-errata

