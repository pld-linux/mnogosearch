#
# Conditional build:
%bcond_with	chasen		# use ChaSen Japanese morphological analisys system
				# (not tested, maybe on by default?)
%bcond_without	expat		# without XML support (using expat library)
%bcond_without	ssl		# without SSL support (using OpenSSL)
# databases
%bcond_without	mysql		# support for MySQL
%bcond_without	pgsql		# support for PostgreSQL
# databases through ODBC
%bcond_with	iodbc		# with ODBC support through iODBC
%bcond_with	unixodbc	# with ODBC support through unixODBC
# databases through FreeTDS
%bcond_with	mssql		# support for MS SQL through FreeTDS
#
Summary:	Another one web indexing and searching system for a small domain or intranet
Summary(pl):	Kolejny system indeksowania i przeszukiwania WWW dla ma³ych domen i intranetu
Name:		mnogosearch
Version:	3.2.32
Release:	1
License:	GPL v2+
Group:		Networking/Utilities
#Source0Download: http://www.mnogosearch.ru/download.html
Source0:	http://www.mnogosearch.ru/Download/%{name}-%{version}.tar.gz
# Source0-md5:	c244702ad4bc95bacf7b06ac1327b159
Source1:	%{name}-dbgen
Patch0:		%{name}-acfixes.patch
URL:		http://www.mnogosearch.ru/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_chasen:BuildRequires:	chasen-devel}
%{?with_expat:BuildRequires:	expat-devel}
%{?with_mssql:BuildRequires:	freetds-devel}
%{?with_iodbc:BuildRequires:	libiodbc-devel}
BuildRequires:	libtool
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7d}
%{?with_pgsql:BuildRequires:	postgresql-devel}
%{?with_unixodbc:BuildRequires:	unixODBC-devel}
BuildRequires:	zlib-devel
PreReq:		webserver
#%{?with_pgsql:PreReq:		postgresql-clients}
Requires:	%{name}-lib = %{version}-%{release}
Obsoletes:	aspseek
Obsoletes:	mnogosearch-stored
Obsoletes:	udmsearch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}
%define		_localstatedir	/var/lib/mnogosearch
%define		_ourdatadir	%{_datadir}/%{name}
%define		htmldir		/home/services/httpd/html
%define		cgidir		/home/services/httpd/cgi-bin

%description
The mnogosearch system is a complete world wide web indexing and
searching system for a small domain or intranet. This system is not
meant to replace the need for powerful internet-wide search systems
like Lycos, Infoseek, Webcrawler and AltaVista. Instead it is meant to
cover the search needs for a single company, campus, or even a
particular sub section of a web site. Features:
- MP3 tag info
- news searching(?)
- http: (and ftp: - via proxy) URL schemaa
- charset guesser
- externel parsers
- support for ssl (https://)
- limiting queries to one hostname by sth like this: <INPUT
  TYPE=HIDDEN NAME=ul VALUE=http://www.something.com/>
- it's posilble to run indexers on several diffrent (theoreticaly 128)
  hosts, and gather information on one of them, reindexing proceses make
  no harm to avalibility of search engine. See cachemode.txt

As opposed to some WAIS-based or web-server based search engines,
mnogsearch can span several web servers at a site. The type of these
different web servers doesn't matter as long as they understand the
HTTP 1.0 protocol. Mnogosearch supports also virtual domains.

%description -l pl
Mnogosearch jest kompletnym systemem indeksuj±cym i przeszukuj±cym WWW
dla ma³ych domen oraz intranetu. System nie zosta³ opracowany jako
wielki system typu Lycos, Infoseek WebCrawler i AltaVista. Natomiast
nadaje siê do zastosowania w pojedynczej firmie, kampusie lub
jakiejkolwiek stronie WWW. Zalety:
- przeszukiwanie tagów MP3,
- niusów (Server news://localhost/pl/),
- htdb czyli baz danych udostêpnianych przez WWW/CGI. (HTDBList SELECT
  \ concat("http://search.mnogo.ru/board/message.php?id=",id) \ FROM
  udm.messages LIMIT 2))
- zawarto¶ci serwerów FTP (rada za 2gr: "Index no" dla serwera FTP
  spowoduje nie indeksowanie *zawarto¶ci* plików na nim siê znajduj±cych)
- wyszukiwanie w zwyk³ych URL-ach http://
- wsparcie dla SSL (https://)
- wyszukiwanie w mirrorach (równie¿ lokalnych) odleg³ych sieci
- zgadywanie zestawu znaków
- zewnêtrzne przetwarzacze dokumentów na potrzeby indeksowania
- ograniczanie zapytañ do jednej nazwy hosta: <INPUT TYPE=HIDDEN
  NAME=ul VALUE=http://www.something.com/>
- kategoryzacja witryny (doc/categories.txt)
- mo¿liwe jest uruchomienie kilku procesów indeksuj±cych na kilku
  (teoretycznie 128) hostach i trzymanie bazy na jednym z nich,
  reindeksacja nie powoduje wtedy niedostêpno¶ci wyszukiwarki.
  Przeczytaj cachemode.txt

W odró¿nieniu od innych systemów bazuj±cych na WAIS-ie lub serwerach
WWW, mnogosearch mo¿e ³±czyæ kilka serwerów WWW w jednym miejscu. Typ
serwera nie ma znaczenia, dopóki pracuje on zgodnie z protoko³em HTTP
1.0. Pakiet wspó³pracuje równie¿ z domenami wirtualnymi.

%package lib
Summary:	mnogosearch library
Summary(pl):	Biblioteka mnogosearch
Group:		Libraries

%description lib
This package contains mnogosearch library files.

%description lib -l pl
Ten pakiet zawiera pliki biblioteki mnogosearch.

%package devel
Summary:	Include files for mnogosearch
Summary(pl):	Pliki nag³ówkowe mnogosearch
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}-%{release}
%{?with_expat:Requires:	expat-devel}
%{?with_iodbc:Requires:	libiodbc-devel}
%{?with_mysql:Requires:	mysql-devel}
%{?with_ssl:Requires:	openssl-devel}
%{?with_pgsql:Requires:	postgresql-devel}
%{?with_unixodbc:Requires:	unixODBC-devel}
Requires:	zlib-devel

%description devel
This package contains mnogosearch development files.

%description devel -l pl
Pliki dla programistów u¿ywaj±cych mnogosearch.

%package static
Summary:	mnogosearch static libraries
Summary(pl):	Biblioteki statyczne mnogosearch
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static libraries of mnogosearch.

%description static -l pl
Ten pakiet zawiera statyczne biblioteki mnogosearch.

%prep
%setup -q
%patch -p1

%build
find . -type d -name CVS | xargs rm -rf
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--datadir=%{_ourdatadir} \
	DOCBOOKSTYLE="/usr/share/sgml/docbook/dsssl-stylesheets" \
	--enable-syslog=LOG_LOCAL6 \
	--enable-charset-guesser \
	%{?with_chasen:--enable-chasen} \
	--enable-fast-cat \
	--enable-fast-tag \
	--enable-fast-site \
	--enable-linux-pthreads \
	--enable-news-extension \
	--enable-phrase \
	--enable-shared \
	--with-built-in \
	--with-cgi-bin-dir=%{cgidir} \
	--with-config-dir=%{_sysconfdir}/http/%{name} \
	%{?with_expat:--with-expat} \
	--with-image-dir=%{htmldir}/%{name} \
	%{?with_mssql:--with-freetds} \
	%{?with_iodbc:--with-iodbc} \
	%{?with_mysql:--with-mysql} \
	%{?with_ssl:--with-openssl} \
	%{?with_pgsql:--with-pgsql} \
	--with-search-dir=%{htmldir} \
	%{?with_unixodbc:--with-unixODBC} \
	--with-zlib

# --with-readline (for SQL monitor) ?
# --wiht-extra-charsets=big5,gb2312,gbk,japanese,euc-kr,gujarati,tscii ?

%{__make}

#  enable automatic Russian charset guesser :-]
# wy uze www.linux.ru procitacli sewodnja?

#  --with-solid[=DIR]      Include Solid support.  DIR is the Solid base
#  --with-openlink[=DIR]   Include OpenLink ODBC support.
#  --with-easysoft[=DIR]   Include EasySoft ODBC support.
#  --with-sapdb[=DIR]      Include SAPDB support.  DIR is the SAPDB base
#  --with-ibase[=DIR]      Include InterBase support.  DIR is the InterBase
#  --with-ctlib[=DIR]      Include Ct-Lib support.
#  --with-freetds[=DIR]    Include FreeTDS Ct-Lib support.
#  --with-oracle7[=DIR]    Include Oracle 7.3 support.  DIR is the Oracle
#  --with-oracle8[=DIR]    Include Oracle8 support.  DIR is the Oracle
#  --with-oracle8i[=DIR]   Include Oracle8i support.  DIR is the Oracle
#
# FIXME: add selection of storage method, spliting into %{name}-common & %{name}-$DB_NAME

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_localstatedir},%{htmldir},%{cgidir},%{_sysconfdir}} \
	$RPM_BUILD_ROOT{/etc/cron.daily,%{_infodir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	doc_FILES='$(HTML_ALL)'

ln -sf %{_defaultdocdir}/%{name}-%{version}/html \
	$RPM_BUILD_ROOT%{htmldir}/mnogodoc

mv -f $RPM_BUILD_ROOT%{_bindir}/*.cgi \
	$RPM_BUILD_ROOT%{cgidir}

install -d $RPM_BUILD_ROOT/usr/src/example/mnogosearch
install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.daily/mnogosearch-dbgen

mkdir html
cp -af doc/*.{html,css} html

cd $RPM_BUILD_ROOT%{_sysconfdir}
touch locals
for f in *-dist ; do
	mv -f $f `basename $f -dist`
done

rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF
Please see docs (%{_defaultdocdir}/%{name}-%{version}),
then read how to setup db connection, and put line like this
"pgsql://user:password@/dbname/" into %{_sysconfdir}, then setup database
using "indexer -Ecreate" command.
EOF

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO html doc/samples
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{cgidir}/*
%{_datadir}/%{name}
%{htmldir}/mnogodoc
%dir %{_localstatedir}
%attr(775,root,http) %{_localstatedir}/cache
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.freq
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.htm
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/locals
%dir %{_sysconfdir}/langmap
%dir %{_sysconfdir}/stopwords
%dir %{_sysconfdir}/synonym
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*/*
%config(noreplace) %attr(750,root,root) /etc/cron.daily/*
%{_mandir}/man?/*

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*-*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/udm-config
%attr(755,root,root) %{_libdir}/libmnogosearch.so
%attr(755,root,root) %{_libdir}/libmnogocharset.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
