%include	/usr/lib/rpm/macros.python
%define		zope_subname	fcForum
Summary:	Message Board Product for Zope
Summary(pl):	Forum dla Zope
Name:		Zope-%{zope_subname}
Version:	2.0.1
Release:	1
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://www.genix.biz/files/%{zope_subname}-2-0-1.tgz
# Source0-md5:	9c74b9b6f532aee732345485301c3c85
URL:		http://www.genix.biz/forum_dev/index_html
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-CookieCrumbler
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	product_dir	/usr/lib/zope/Products

%description
Message Board Product for Zope.

%description -l pl
Forum dla Zope.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

cp -af {Extensions,www,*.py} $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc filelist.txt
%{product_dir}/%{zope_subname}
