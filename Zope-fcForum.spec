%include	/usr/lib/rpm/macros.python
%define		zope_subname	fcForum
Summary:	Message Board Product for Zope
Summary(pl):	Forum dla Zope
Name:		Zope-%{zope_subname}
Version:	2.0.5
Release:	2
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://www.genixsys.com/files/%{zope_subname}-2-0-5.tgz
# Source0-md5:	c446824e3c12ad960444325929c6bb1a
URL:		http://www.genixsys.com/forum_dev/index_html
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-CookieCrumbler
Requires(post,postun):  /usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Message Board Product for Zope.

%description -l pl
Forum dla Zope.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {www,*.py,refresh.txt,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname} 
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc filelist.txt
%{_datadir}/%{name}
