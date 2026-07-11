%global tl_name graphics-pln
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX-style graphics for Plain TeX users
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/graphics
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics-pln.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics-pln.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Plain TeX graphics package is mostly a thin shell around the LaTeX
graphicx and color packages, with support of the LaTeX-isms in those
packages provided by miniltx (which is the largest part of the bundle).
The bundle also contains a file picture.tex, which is a wrapper around
the autopict.sty, and provides the LaTeX picture mode to Plain TeX
users.

