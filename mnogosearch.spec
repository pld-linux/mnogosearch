Summary:	A another one web indexing and searching system for a small domain or intranet
Summary(pl):	Kolejny System indeksowania i przeszukiwania www dla ma³ych domen i intranetu
Name:		mnogosearch
Version:	3.1.16
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Source0:	http://www.mnogosearch.ru/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.mnogosearch.ru/
BuildRequires:	postgresql-devel
PreReq:		webserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/http/%{name}
%define		_localstatedir	/var/lib/mnogosearch

%description
The mnogosearch system is a complete world wide web indexing and
searching system for a small domain or intranet. This system is not
meant to replace the need for powerful internet-wide search systems
like Lycos, Infoseek, Webcrawler and AltaVista. Instead it is meant to
cover the search needs for a single company, campus, or even a
particular sub section of a web site. Features:
 - mp3 tag info
 - news searching(?)
 - http: (and ftp: - via proxy) URL schemaa
 - charset guesser
 - externel parsers

As opposed to some WAIS-based or web-server based search engines,
ht://Dig can span several web servers at a site. The type of these
different web servers doesn't matter as long as they understand the
HTTP 1.0 protocol.

%description -l pl
Mnogosearch jest kompletnym systemem indeksuj±cym i przeszukuj±cym www
dla ma³ych domen oraz intranetu. System nie zosta³ opracowany jako
wielki system typu Lycos, Infoseek WebCrawler i AltaVista. Natomiast
nadeje siê do zastosowania w pojedyñczej firmie, kampusie lub
jakiejkolwiek stronie www.

W odró¿nieniu do innych bazuj±cych na WAIS-sie lub serwerch www
systemach, mnogosearch mo¿e ³±czyæ kilka serwerów www w jednym
miejscu. Typ serwera nie ma znaczenia, dopóki pracuje on zgodnie z
protoko³em HTTP 1.0

%package devel
Summary:	Include files and libraries for htdig
Summary(pl):	Pliki nag³ówkowe dla htdig
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The ht://Dig system is a complete world wide web indexing and
searching system for a small domain or intranet. This system is not
meant to replace the need for powerful internet-wide search systems
like Lycos, Infoseek, Webcrawler and AltaVista. Instead it is meant to
cover the search needs for a single company, campus, or even a
particular sub section of a web site.

As opposed to some WAIS-based or web-server based search engines,
ht://Dig can span several web servers at a site. The type of these
different web servers doesn't matter as long as they understand the
HTTP 1.0 protocol.

This package contains devlopment files.

%package pgsql
Summary:	mnogosearch w/ pgsql storage-support 
Summary(pl):	mnogosearch z pgsqlem jako metod± przechowywania danych
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Requires:	%{name} = %{version}

%description pgsql
The ht://Dig system is a complete world wide web indexing and
searching system for a small domain or intranet. This system is not
meant to replace the need for powerful internet-wide search systems
like Lycos, Infoseek, Webcrawler and AltaVista. Instead it is meant to
cover the search needs for a single company, campus, or even a
particular sub section of a web site.

As opposed to some WAIS-based or web-server based search engines,
ht://Dig can span several web servers at a site. The type of these
different web servers doesn't matter as long as they understand the
HTTP 1.0 protocol.

This package contains pgsql storage support.

%package static
Summary:	htdig static libraries
Summary(pl):	Biblioteki statyczne htdig
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
The ht://Dig system is a complete world wide web indexing and
searching system for a small domain or intranet. This system is not
meant to replace the need for powerful internet-wide search systems
like Lycos, Infoseek, Webcrawler and AltaVista. Instead it is meant to
cover the search needs for a single company, campus, or even a
particular sub section of a web site. As opposed to some WAIS-based or
web-server based search engines, ht://Dig can span several web servers
at a site. The type of these different web servers doesn't matter as
long as they understand the HTTP 1.0 protocol. This package contains
static libraries of htdig.

%prep
%setup -q
%patch0 -p1

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure \
	--enable-syslog      \
	--enable-syslog=LOG_LOCAL6 \
	--with-image-dir=/home/httpd/html/%{name} \
	--with-cgi-bin-dir=/home/httpd/cgi-bin \
	--with-search-dir=/home/httpd/html \
	--with-config-dir=%{_sysconfdir}/http/%{name} \
	--with-pgsql \
	--with-openssl \
	--enable-linux-pthreads \
	--enable-charset-guesser \
	--enable-news-extension \
	--enable-fast-tag \
	--enable-fast-cat \
	--enable-fast-site \
	--enable-phrase         

#  enable automatic Russian charset guesser :-]
# wy uze www.linux.ru procitacli sewodnja?

#  --with-msql[=DIR]       Include mSQL support.  DIR is the mSQL base
#  --with-iodbc[=DIR]      Include iODBC support.  DIR is the iODBC base
#  --with-unixODBC[=DIR]   Include unixODBC support.  DIR is the unixODBC base
#  --with-solid[=DIR]      Include Solid support.  DIR is the Solid base
#  --with-openlink[=DIR]   Include OpenLink ODBC support. 
#  --with-easysoft[=DIR]   Include EasySoft ODBC support. 
#  --with-sapdb[=DIR]      Include SAPDB support.  DIR is the SAPDB base
#  --with-ibase[=DIR]      Include InterBase support.  DIR is the InterBase
#  --with-oracle7[=DIR]    Include Oracle 7.3 support.  DIR is the Oracle
#  --with-oracle8[=DIR]    Include Oracle8 support.  DIR is the Oracle
#  --with-oracle8i[=DIR]   Include Oracle8i support.  DIR is the Oracle
#	--with-buildin \
#	--with-mysql \
#	
# FIXME: add selection of storage method, spliting into %{name}-common & %{name}-$DB_NAME

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/lib/mnogosearch,/etc/cron.daily} \
	$RPM_BUILD_ROOT/home/httpd/html/%{name}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

ln -sf ../..%{_bindir}/rundig \
	$RPM_BUILD_ROOT/etc/cron.daily/{%name}-dbgen

ln -sf ../../../..%{_defaultdocdir}/%{name}-%{version} \
        $RPM_BUILD_ROOT/home/httpd/html/%{name}/mnogodoc

install etc/search.htm-dist $RPM_BUILD_ROOT/home/httpd/html/search.html

ln -sf  $RPM_BUILD_ROOT%{_bindir}/search.cgi $RPM_BUILD_ROOT/home/httpd/cgi-bin/search.cgi

%clean
rm -rf $RPM_BUILD_ROOT

%post
# Only run this if installing for the first time
#if [ "$1" = 1 ]; then
#	for i in `grep '^ServerName' /etc/httpd/httpd.conf | sort -u | awk '{print $2}'`; do echo -n http://$i/; echo -n " "; done > /tmp/htdig.tmp
#	SERVERNAMES="`cat /tmp/htdig.tmp`"
#	[ -z "$SERVERNAMES" ] && SERVERNAMES="`hostname -f`"
#	[ -z "$SERVERNAMES" ] && SERVERNAMES="localhost"
#	SERVERNAME=`grep '^ServerName' /etc/httpd/httpd.conf | uniq -d | awk '{print $2}'`
#	grep -v -e local_urls -e local_user_urls -e start_url /etc/htdig/htdig.conf > /tmp/htdig.tmp
#	mv -f /tmp/htdig.tmp /etc/htdig/htdig.conf
#	echo "start_url:$SERVERNAMES
#local_urls:		$SERVERNAMES
#local_user_urls:	http://$SERVERNAME/=/home/,/public_html/" >> /etc/htdig/htdig.conf
#
#fi

%files
%defattr(644,root,root,755)
%doc COPYING README doc/*
%dir /var/lib/%{name}
# maybe user== nobody ?
%attr (755,http,http) /home/httpd/cgi-bin/*
%attr (755,root,root) %{_bindir}/*
%attr (755,root,root) %{_libdir}/%{name}/*so
%attr (755,root,root) %{_libdir}/%{name}/*la
/home/httpd/html/%{name}/*
%{_datadir}/%{name}/*
%config(noreplace) %{_sysconfdir}/html/%{name}/*
%config(missingok noreplace) %verify(not size mtime md5) /home/httpd/html/search.html
#%config(missingok) %{_sysconfdir}/cron.daily/htdig-dbgen

#%files devel
#%defattr(644,root,root,755)
#%{_includedir}/%{name}/*

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/%{name}/*.a
