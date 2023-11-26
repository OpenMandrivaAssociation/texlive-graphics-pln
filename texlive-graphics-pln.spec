Name:		texlive-graphics-pln
Version:	68760
Release:	1
Summary:	LaTeX-style graphics for Plain TeX users
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/graphics
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics-pln.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics-pln.doc.r%{version}.tar.xz
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

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
