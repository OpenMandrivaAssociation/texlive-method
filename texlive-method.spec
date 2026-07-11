%global tl_name method
%global tl_revision 17485

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0b
Release:	%{tl_revision}.1
Summary:	Typeset method and variable declarations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/method
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/method.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/method.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/method.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package supports typesetting of programming language method and
variable declarations. It supports declarations in German, French and
English.

