%global octpkg sole

Summary:	A package for transient and steady state simulation of organic solar cells
Name:		octave-sole
Version:	0.1.1
Release:	2
License:	GPLv2+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/sole/
Url:		https://sourceforge.net/p/sole/
Source0:	https://downloads.sourceforge.net/sole/sole-%{version}.tar.gz

BuildRequires:  octave-devel >= 7.3.0
BuildRequires:  octave-bim >= 1.0.0

Requires:	octave(api) = %{octave_api}
Requires:  	octave-bim >= 1.0.0

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
A package for transient and steady state simulation of organic solar 
cells.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

