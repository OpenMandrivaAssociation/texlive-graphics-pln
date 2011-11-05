# revision 16917
# category Package
# catalog-ctan /macros/plain/graphics
# catalog-date 2010-01-03 16:55:09 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-graphics-pln
Version:	20100103
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The Plain TeX graphics package is mostly a thin shell around
the LaTeX graphicx and color packages, with support of the
LaTeX-isms in those packages provided by miniltx (which is the
largest part of the bundle). The bundle also contains a file
"picture.tex", which is a wrapper around the autopict.sty, and
provides the LaTeX picture mode to Plain TeX users.

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
%{_texmfdistdir}/tex/plain/graphics-pln/autopict.sty
%{_texmfdistdir}/tex/plain/graphics-pln/color.tex
%{_texmfdistdir}/tex/plain/graphics-pln/graphicx.tex
%{_texmfdistdir}/tex/plain/graphics-pln/miniltx.tex
%{_texmfdistdir}/tex/plain/graphics-pln/picture.tex
%{_texmfdistdir}/tex/plain/graphics-pln/psfrag.tex
%doc %{_texmfdistdir}/doc/plain/graphics-pln/00readme.txt
%doc %{_texmfdistdir}/doc/plain/graphics-pln/exmplcol.tex
%doc %{_texmfdistdir}/doc/plain/graphics-pln/exmplgrf.tex
%doc %{_texmfdistdir}/doc/plain/graphics-pln/exmplpfg.tex
%doc %{_texmfdistdir}/doc/plain/graphics-pln/exmplpic.tex
#- source
%doc %{_texmfdistdir}/source/plain/graphics-pln/autopict.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
