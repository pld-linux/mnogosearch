# TODO: webapps?
#
# Conditional build:
%bcond_with	chasen		# use ChaSen Japanese morphological analysis system (not tested, maybe on by default?)
%bcond_without	ssl		# without SSL support (using OpenSSL)
%bcond_with	mecab		# use mecab Japanese morphological system
# databases
%bcond_without	mysql		# support for MySQL
%bcond_without	pgsql		# support for PostgreSQL
%bcond_with	sqlite		# support for SQLite 2.x
%bcond_without	sqlite3		# support for SQLite 3.x
%bcond_with	ibase		# support for InterBase/Firebird
# databases through ODBC
%bcond_with	iodbc		# with ODBC support through iODBC
%bcond_with	unixodbc	# with ODBC support through unixODBC
# databases through FreeTDS
%bcond_without	freetds		# support for Sybase/MS SQL through FreeTDS

Summary:	Another one web indexing and searching system for a small domain or intranet
Summary(pl.UTF-8):	Kolejny system indeksowania i przeszukiwania WWW dla małych domen i intranetu
Name:		mnogosearch
Version:	3.3.14
Release:	5
License:	GPL v2+
Group:		Networking/Utilities
# Source0Download: http://www.mnogosearch.org/download.html
Source0:	http://www.mnogosearch.org/Download/%{name}-%{version}.tar.gz
# Source0-md5:	caf042f31134ae1304f0963a9f4964a9
Source1:	%{name}-dbgen
Patch0:		%{name}-acfixes.patch
Patch1:		%{name}-as_needed-fix.patch
URL:		http://www.mnogosearch.org/
%{?with_ibase:BuildRequires:	Firebird-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_chasen:BuildRequires:	chasen-devel}
%{?with_freetds:BuildRequires:	freetds-devel}
%{?with_iodbc:BuildRequires:	libiodbc-devel}
BuildRequires:	libtool
%{?with_mecab:BuildRequires:	mecab-devel}
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7d}
%{?with_pgsql:BuildRequires:	postgresql-devel}
%{?with_sqlite:BuildRequires:	sqlite-devel}
%{?with_sqlite3:BuildRequires:	sqlite3-devel}
%{?with_unixodbc:BuildRequires:	unixODBC-devel}
BuildRequires:	zlib-devel
Requires:	%{name}-lib = %{version}-%{release}
Requires:	webserver
Obsoletes:	aspseek
Obsoletes:	mnogosearch-stored
Obsoletes:	udmsearch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}
%define		_localstatedir	/var/lib/mnogosearch
%define		cgidir		/usr/lib/cgi-bin

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
- it's possilble to run indexers on several different (theoreticaly
  128) hosts, and gather information on one of them, reindexing proceses
  make no harm to avalibility of search engine. See cachemode.txt

As opposed to some WAIS-based or web-server based search engines,
mnogsearch can span several web servers at a site. The type of these
different web servers doesn't matter as long as they understand the
HTTP 1.0 protocol. Mnogosearch supports also virtual domains.

%description -l pl.UTF-8
Mnogosearch jest kompletnym systemem indeksującym i przeszukującym WWW
dla małych domen oraz intranetu. System nie został opracowany jako
wielki system typu Lycos, Infoseek WebCrawler i AltaVista. Natomiast
nadaje się do zastosowania w pojedynczej firmie, kampusie lub
jakiejkolwiek stronie WWW. Zalety:
- przeszukiwanie znaczników MP3,
- niusów (Server news://localhost/pl/),
- htdb czyli baz danych udostępnianych przez WWW/CGI. (HTDBList SELECT
  \ concat("http://search.mnogo.ru/board/message.php?id=",id) \ FROM
  udm.messages LIMIT 2))
- zawartości serwerów FTP (rada za 2gr: "Index no" dla serwera FTP
  spowoduje nie indeksowanie *zawartości* plików na nim się
  znajdujących)
- wyszukiwanie w zwykłych URL-ach http://
- wsparcie dla SSL (https://)
- wyszukiwanie w mirrorach (również lokalnych) odległych sieci
- zgadywanie zestawu znaków
- zewnętrzne przetwarzacze dokumentów na potrzeby indeksowania
- ograniczanie zapytań do jednej nazwy hosta: <INPUT TYPE=HIDDEN
  NAME=ul VALUE=http://www.something.com/>
- kategoryzacja witryny (doc/categories.txt)
- możliwe jest uruchomienie kilku procesów indeksujących na kilku
  (teoretycznie 128) hostach i trzymanie bazy na jednym z nich,
  reindeksacja nie powoduje wtedy niedostępności wyszukiwarki.
  Przeczytaj cachemode.txt

W odróżnieniu od innych systemów bazujących na WAIS-ie lub serwerach
WWW, mnogosearch może łączyć kilka serwerów WWW w jednym miejscu. Typ
serwera nie ma znaczenia, dopóki pracuje on zgodnie z protokołem HTTP
1.0. Pakiet współpracuje również z domenami wirtualnymi.

%package lib
Summary:	mnogosearch library
Summary(pl.UTF-8):	Biblioteka mnogosearch
Group:		Libraries

%description lib
This package contains mnogosearch library files.

%description lib -l pl.UTF-8
Ten pakiet zawiera pliki biblioteki mnogosearch.

%package devel
Summary:	Include files for mnogosearch
Summary(pl.UTF-8):	Pliki nagłówkowe mnogosearch
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}-%{release}
%{?with_ibase:Requires:	Firebird-devel}
%{?with_chasen:Requires:	chasen-devel}
%{?with_freetds:Requires:	freetds-devel}
%{?with_iodbc:Requires:	libiodbc-devel}
%{?with_mecab:Requires:	mecab-devel}
%{?with_mysql:Requires:	mysql-devel}
%{?with_ssl:Requires:	openssl-devel}
%{?with_pgsql:Requires:	postgresql-devel}
%{?with_sqlite:Requires:	sqlite-devel}
%{?with_sqlite3:Requires:	sqlite3-devel}
%{?with_unixodbc:Requires:	unixODBC-devel}
Requires:	zlib-devel

%description devel
This package contains mnogosearch development files.

%description devel -l pl.UTF-8
Pliki dla programistów używających mnogosearch.

%package static
Summary:	mnogosearch static libraries
Summary(pl.UTF-8):	Biblioteki statyczne mnogosearch
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static libraries of mnogosearch.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczne biblioteki mnogosearch.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
find . -type d -name CVS | xargs rm -rf
%{__libtoolize}
%{__aclocal} -I build/m4
%{__autoconf}
%{__automake}
%configure \
	DOCBOOKSTYLE="/usr/share/sgml/docbook/dsssl-stylesheets" \
	--datadir=%{_datadir}/%{name} \
	--enable-syslog=LOG_LOCAL6 \
	%{?with_chasen:--with-chasen} \
	%{?with_freetds:--with-freetds} \
	%{?with_ibase:--with-ibase} \
	%{?with_iodbc:--with-iodbc} \
	%{?with_mecab:--with-mecab} \
	%{?with_mysql:--with-mysql} \
	%{?with_ssl:--with-openssl} \
	%{?with_pgsql:--with-pgsql} \
	%{?with_sqlite:--with-sqlite} \
	%{?with_sqlite3:--with-sqlite3} \
	%{?with_unixodbc:--with-unixODBC} \
	--with-zlib

# --enable-mysql-fulltext-plugin ?
# --with-readline (for SQL monitor) ?
# --wiht-extra-charsets=big5,gb2312,gbk,japanese,euc-kr,gujarati,tscii ?

%{__make} -j1 -C src libmnogocharset.la
%{__make} -j1

#  --with-solid[=DIR]	  Include Solid support.  DIR is the Solid base
#  --with-openlink[=DIR]   Include OpenLink ODBC support.
#  --with-easysoft[=DIR]   Include EasySoft ODBC support.
#  --with-sapdb[=DIR]	  Include SAPDB support.  DIR is the SAPDB base
#  --with-ctlib[=DIR]	  Include Ct-Lib support.
#  --with-oracle7[=DIR]	Include Oracle 7.3 support.  DIR is the Oracle
#  --with-oracle8[=DIR]	Include Oracle8 support.  DIR is the Oracle
#  --with-oracle8i[=DIR]   Include Oracle8i support.  DIR is the Oracle
#
# FIXME: add selection of storage method, spliting into %{name}-common & %{name}-$DB_NAME

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_localstatedir},%{cgidir},%{_sysconfdir}} \
	$RPM_BUILD_ROOT{/etc/cron.daily,%{_infodir}}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	doc_FILES='$(HTML_ALL)'

mv -f $RPM_BUILD_ROOT%{_bindir}/search.cgi \
	$RPM_BUILD_ROOT%{cgidir}/mnogosearch.cgi

install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.daily/mnogosearch-dbgen

mkdir html
cp -af doc/*.{html,css} html

cd $RPM_BUILD_ROOT%{_sysconfdir}
touch locals
for f in *-dist ; do
	mv -f $f `basename $f -dist`
done

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/mnogosearch

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF
Please see docs (%{_docdir}/%{name}-%{version}),
then read how to setup db connection, and put line like this
"pgsql://user:password@/dbname/" into %{_sysconfdir}, then setup database
using "indexer -Ecreate" command.
EOF

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO html doc/samples
%attr(755,root,root) %{_sbindir}/indexer
%attr(755,root,root) %{_bindir}/mconv
%attr(755,root,root) %{_bindir}/mguesser
%attr(755,root,root) %{cgidir}/mnogosearch.cgi
%{_datadir}/%{name}
%attr(775,root,http) %dir %{_localstatedir}
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/indexer.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/langmap.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/stopwords.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.freq
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/search.htm
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/node.xml
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/locals
%dir %{_sysconfdir}/langmap
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/langmap/*.lm
%dir %{_sysconfdir}/stopwords
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/stopwords/*.sl
%dir %{_sysconfdir}/synonym
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/synonym/*.syn
%config(noreplace) %attr(750,root,root) /etc/cron.daily/mnogosearch-dbgen
%{_mandir}/man1/indexer.1*
%{_mandir}/man5/indexer.conf.5*

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmnogocharset-3.3.so
%attr(755,root,root) %{_libdir}/libmnogosearch-3.3.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/udm-config
%attr(755,root,root) %{_libdir}/libmnogocharset.so
%attr(755,root,root) %{_libdir}/libmnogosearch.so
%{_libdir}/libmnogocharset.la
%{_libdir}/libmnogosearch.la
%{_includedir}/udmsearch.h
%{_includedir}/udm_*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libmnogocharset.a
%{_libdir}/libmnogosearch.a
