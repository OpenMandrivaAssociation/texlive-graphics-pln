Name:		texlive-graphics-pln
Version:	20170612
Release:	1
Summary:	LaTeX-style graphics for Plain TeX users
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/graphics
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics-pln.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics-pln.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics-pln.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Plain TeX graphics package is mostly a thin shell around
the LaTeX graphicx and color packages, with support of the
LaTeX-isms in those packages provided by miniltx (which is the
largest part of the bundle). The bundle also contains a file
"picture.tex", which is a wrapper around the autopict.sty, and
provides the LaTeX picture mode to Plain TeX users.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/graphics-pln
%doc %{_texmfdistdir}/doc/plain/graphics-pln
#- source
%doc %{_texmfdistdir}/source/plain/graphics-pln

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
