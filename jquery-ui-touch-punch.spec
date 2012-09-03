%define		plugin	touch-punch
Summary:	Touch Event Support for jQuery UI
Name:		jquery-ui-%{plugin}
Version:	0.2.2
Release:	1
License:	MIT or GPL v2
Group:		Applications/WWW
Source0:	https://github.com/furf/jquery-ui-touch-punch/tarball/master/%{name}-%{version}.tgz
# Source0-md5:	e1d0c6664da0b889fcea1a17d21c3e80
URL:		http://touchpunch.furf.com/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
# depends: jquery.ui.widget.js, jquery.ui.mouse.js
Requires:	jquery-ui
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/ui/%{plugin}

%description
jQuery UI Touch Punch is a small hack that enables the use of touch
events on sites using the jQuery UI user interface library.

%prep
%setup -qc
mv *-%{plugin}-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p jquery.ui.%{plugin}.min.js  $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p jquery.ui.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{_appdir}
