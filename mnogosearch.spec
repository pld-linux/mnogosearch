#
# Conditional build:
# _with_pgsql	support for postgres
# _with_mysql	support for mysql
#
Summary:	Another one web indexing and searching system for a small domain or intranet
Summary(pl):	Kolejny System indeksowania i przeszukiwania www dla ma³ych domen i intranetu
Name:		mnogosearch
Version:	3.2.6
Release:	3
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.mnogosearch.ru/Download/%{name}-%{version}.tar.gz
Source1:	%{name}-gethostnames
Source2:	%{name}-Mysql-database
Source3:	%{name}-stored.init
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-Mysql-pld.patch
Patch2:		%{name}-stored-dirs_1.patch
URL:		http://www.mnogosearch.ru/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
%{?_with_mysql:BuildRequires:	mysql-devel}
BuildRequires:	openssl-devel
%{?_with_pgsql:BuildRequires:	postgresql-devel}
Prereq:		webserver
%{?_with_pgsql:Prereq:		postgresql-clients}
Requires:	%{name}-lib = %{version}
Obsoletes:	udmsearch
Obsoletes:	aspseek
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}
%define		_localstatedir	/var/lib/mnogosearch
%define		htmldir		/home/httpd/html
%define		cgidir		/home/httpd/cgi-bin

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
Mnogosearch jest kompletnym systemem indeksuj±cym i przeszukuj±cym www
dla ma³ych domen oraz intranetu. System nie zosta³ opracowany jako
wielki system typu Lycos, Infoseek WebCrawler i AltaVista. Natomiast
nadaje siê do zastosowania w pojedynczej firmie, kampusie lub
jakiejkolwiek stronie www. Zalety:
 - przeszukiwaie tagów mp3,
 - niusów (Server news://localhost/pl/),
 - htdb czyli baz danych udostêpnianych przez www/cgi. (HTDBList SELECT
   \ concat("http://search.mnogo.ru/board/message.php?id=",id) \ FROM
   udm.messages LIMIT 2))
 - zawarto¶ci serwerów ftp (rada za 2gr: "Index no" dla serwera ftp
   spowoduje nie indexowanie *zawarto¶ci* plików na nim siê znajduj±cych)
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
www, mnogosearch mo¿e ³±czyæ kilka serwerów www w jednym miejscu. Typ
serwera nie ma znaczenia, dopóki pracuje on zgodnie z protoko³em HTTP
1.0. Pakiet wspó³pracuje równie¿ z domenami wirtualnymi.

%package lib
Summary:	mnogosearch library
Summary(pl):	Biblioteka mnogosearch
Group:		Libraries
Requires(post):	/sbin/ldconfig

%description lib
This package contains mnogosearch library files.

%description lib -l pl
Ten pakiet zawiera pliki biblioteki mnogosearch.

%package devel
Summary:	Include files for mnogosearch
Summary(pl):	Pliki nag³ówkowe mnogosearch
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}

%description devel
This package contains mnogosearch development files.

%description devel -l pl
Pliki dla programistów u¿ywaj±cych mnogosearch.

%package static
Summary:	mnogosearch static libraries
Summary(pl):	Biblioteki statyczne mnogosearch
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static libraries of mnogosearch.

%description static -l pl
Ten pakiet zawiera statyczne biblioteki mnogosearch.

%package pgsql
Summary:	pgsql storage-support for mnogosearch
Summary(pl):	Obs³uga przechowywania danych w bazie PostgreSQL
Group:		Networking/Utilities
Requires:	%{name} = %{version}

%description pgsql
This package contains PostgreSQL storage support.

Note: install will try to create tables in database mnogosearch.

%description pgsql -l pl
Ten pakiet zawiera obs³ugê baz PostgreSQL do przechowywania
informacji.

Instalacja tego pakietu spowoduje za³o¿enie tabel w bazie mnogosearch.

%package stored
Summary:	Deamon for saving gziped versions of documents.
Summary(pl):	Demon zapisuj±cy zgzipowane wersje dokumentów
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description stored
This package contains optional part of mnogosearch stored daemon,
which stores locally gziped versions of parsed (& indexed) html files,
news articles, etc.

%description stored -l pl
Pakiet zawiera opcjonaln± czê¶æ mnogosearch demon stored, zajmuj±cy
siê lokalnym przechowywaniem przetworzonych (i zindeksowanych)
spakowanych wersji plików html, artyku³ów usenetu, itp.

%prep
%setup -q
%patch0 -p0
#%patch1 -p0
%patch2 -p0

%build
find . -type d -name CVS | xargs rm -rf
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

db="--with-built-in"

%{?_with_mysql: db="--with-mysql"}
%{?_with_pgsql: db="--with-pgsql"}

%configure \
	--enable-syslog      \
	--enable-syslog=LOG_LOCAL6 \
	--with-image-dir=/home/httpd/html/%{name} \
	--with-cgi-bin-dir=/home/httpd/cgi-bin \
	--with-search-dir=/home/httpd/html \
	--with-config-dir=%{_sysconfdir}/http/%{name} \
	--with-openssl \
	$db \
	--enable-linux-pthreads \
	--enable-charset-guesser \
	--enable-news-extension \
	--enable-fast-tag \
	--enable-fast-cat \
	--enable-fast-site \
	--enable-phrase \
	--enable-shared \
	--with-zlib		\
#	--enable-dmalloc

%{__make}

#  enable automatic Russian charset guesser :-]
# wy uze www.linux.ru procitacli sewodnja?

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
#	
# FIXME: add selection of storage method, spliting into %{name}-common & %{name}-$DB_NAME

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_localstatedir},%{htmldir},%{cgidir},%{_sysconfdir}} \
	$RPM_BUILD_ROOT{/etc/cron.daily,%{_infodir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf %{_sbindir}/indexer \
	$RPM_BUILD_ROOT/etc/cron.daily/mnogo-dbgen

ln -sf %{_defaultdocdir}/%{name}-%{version}/html \
        $RPM_BUILD_ROOT%{htmldir}/mnogodoc

mv -f $RPM_BUILD_ROOT%{_bindir}/*.cgi \
	$RPM_BUILD_ROOT/home/httpd/cgi-bin

(cd $RPM_BUILD_ROOT%{_sysconfdir}
touch locals
for f in *-dist ; do
	mv -f $f `basename $f -dist`
done
)

install %{SOURCE1} \
	$RPM_BUILD_ROOT/etc/cron.daily/mnogosearch-gethostnames
install -d $RPM_BUILD_ROOT/usr/src/example/mnogosearch
install %{SOURCE2} $RPM_BUILD_ROOT/usr/src/example/mnogosearch/mysql.sql

install -d $RPM_BUILD_ROOT/etc/rc.d/init.d/
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/mnogosearch-stored

cat > $RPM_BUILD_ROOT/usr/src/example/mnogosearch/pg-sql.sql <<EOF
\connect template1
CREATE DATABASE mnogosearch;
\connect mnogosearch
EOF
cat pgsql/{create,crc-multi,news-extension}.txt >> pgsql/mnogosearch-all.sql
cat >> pgsql/mnogosearch-all.sql <<EOF
CREATE USER "mnogosearch" WITH PASSWORD 'aqq123' NOCREATEDB NOCREATEUSER;
GRANT ALL ON url,dict,robots,stopword,categories,next_url_id,affix TO mnogosearch;
GRANT ALL ON ndict,server,thread,spell,next_cat_id,next_server_id,next_url_id TO mnogosearch;
GRANT ALL ON ndict2,ndict3,ndict4,ndict5,ndict6,ndict7,ndict8,ndict9,
ndict10,ndict11,ndict12,ndict16,ndict32 TO mnogosearch;
GRANT ALL ON dict2,dict3,dict4,dict5,dict6,dict7,dict8,dict9,dict10,
dict11,dict12,dict16,dict32 TO mnogosearch;
GRANT ALL ON "qtrack" TO mnogosearch;
EOF

mkdir html
mv -f doc/*.html html

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF
Please see docs (%{_defaultdocdir}/%{name}-%{version} or http://localhost/mnogodoc),
then read how to setup db connection, and put line like this
"pgsql://user:password@/dbname/" into %{_sysconfdir}, then setup database
by something like "psql < %{_defaultdocdir}/%{name}-%{version}/create/pgsql/*.txt"
EOF

%postun	lib -p /sbin/ldconfig
%post	lib -p /sbin/ldconfig

%post pgsql
echo "Creating database mnogosearch..."
su postgres -c "psql -U postgres template1 < %{_docdir}/%{name}-%{version}/create/pgsql/mnogosearch-all.psql"
echo "Mnogosearch user was created with passwd aqq123 - change it!"

%postun pgsql
echo -n 'Dropping Database mnogosearch:' 
su postgres -c "psql -U postgres template1 -c 'DROP DATABASE mnogosearch;' "

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO html doc/samples
# instructions for database creation
%doc db2 ibase msql mysql oracle pgsql sapdb solid sybase virtuoso
%attr(755,root,root) %{_sbindir}/[^s]*
%attr(755,root,root) %{_sbindir}/s[^t]*
%attr(755,root,root) %{cgidir}/*
%{htmldir}/mnogodoc
%dir %{_localstatedir}
%{_localstatedir}/raw
%{_localstatedir}/splitter
%{_localstatedir}/tree
%attr(775,root,http) %{_localstatedir}/cache
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*.htm
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/locals
%dir %{_sysconfdir}/langmap
%dir %{_sysconfdir}/stopwords
%dir %{_sysconfdir}/synonym
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*/*
%config(noreplace) %attr(750,root,root) /etc/cron.daily/*
%{_mandir}/man?/*

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*-*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/udm-config
%{_includedir}/*
%attr(755,root,root) %{_libdir}/libudmsearch.so
%{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files stored
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/stored
%{_localstatedir}/store
/etc/rc.d/init.d/mnogosearch-stored
