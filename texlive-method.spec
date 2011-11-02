Name:		texlive-method
Version:	20100314
Release:	1
Summary:	Typeset method and variable declarations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/method
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/method.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/method.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/method.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This LaTeX package supports the typesetting of programming
language method and variable declarations. It includes an
option to typeset in French.

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
%{_texmfdistdir}/tex/latex/method/method.sty
%doc %{_texmfdistdir}/doc/latex/method/README
%doc %{_texmfdistdir}/doc/latex/method/method.pdf
%doc %{_texmfdistdir}/doc/latex/method/methtest.tex
#- source
%doc %{_texmfdistdir}/source/latex/method/Makefile
%doc %{_texmfdistdir}/source/latex/method/method.dtx
%doc %{_texmfdistdir}/source/latex/method/method.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
