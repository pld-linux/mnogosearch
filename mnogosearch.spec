# conditional build:
# _pgsql support for postgres
# _mysql support for mysql

Summary:	A another one web indexing and searching system for a small domain or intranet
Summary(pl):	Kolejny System indeksowania i przeszukiwania www dla ma≥ych domen i intranetu
Name:		mnogosearch
Version:	3.2.3
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/NarzÍdzia
Group(pt_BR):	Rede/Utilit·rios
Source0:	http://www.mnogosearch.ru/Download/%{name}-%{version}.tar.gz
Source2:	%{name}-gethostnames
%{?_mysql:Source1:		%{name}-Mysql-database}
Patch0:		%{name}-DESTDIR.patch
%{?_mysql:Patch1:		%{name}-Mysql-pld.patch}
URL:		http://www.mnogosearch.ru/
%{?_pgsql:BuildRequires:	postgresql-devel}
%{?_mysql:BuildRequires:	mysql-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Prereq:		webserver
%{?_pgsql:Prereq:		postgresql-clients}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/httpd/%{name}
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
 - support for ssl (https://)
 - limiting queries to one hostname by sth like this:
   <INPUT TYPE=HIDDEN NAME=ul VALUE=http://www.something.com/>
 - it's posilble to run indexers on several diffrent (theoreticaly 128)
   hosts, and gather information on one of them, reindexing proceses make
   no harm to avalibility of search engine. See cachemode.txt

As opposed to some WAIS-based or web-server based search engines,
mnogsearch can span several web servers at a site. The type of these
different web servers doesn't matter as long as they understand the
HTTP 1.0 protocol. Mnogosearch supports also virtual domains.

%description -l pl
Mnogosearch jest kompletnym systemem indeksuj±cym i przeszukuj±cym www
dla ma≥ych domen oraz intranetu. System nie zosta≥ opracowany jako
wielki system typu Lycos, Infoseek WebCrawler i AltaVista. Natomiast
nadaje siÍ do zastosowania w pojedynczej firmie, kampusie lub
jakiejkolwiek stronie www. Zalety:
 - przeszukiwaie tagÛw mp3,
 - niusÛw (Server news://localhost/pl/),
 - htdb czyli baz danych udostÍpnianych przez www/cgi. (HTDBList SELECT \
   concat("http://search.mnogo.ru/board/message.php?id=",id) \ 
   FROM udm.messages LIMIT 2))
 - zawarto∂ci serwerÛw ftp (rada za 2gr: "Index no" dla serwera ftp
   spowoduje nie indexowanie *zawarto∂ci* plikÛw na nim siÍ znajduj±cych)
 - wyszukiwanie w zwyk≥ych URL-ach http:// 
 - wsparcie dla SSL (https://)
 - wyszukiwanie w mirrorach (rÛwnieø lokalnych) odleg≥ych sieci
 - zgadywanie zestawu znakÛw
 - zewnÍtrzne przetwarzacze dokumentÛw na potrzeby indeksowania
 - ograniczanie zapytaÒ do jednej nazwy hosta:
   <INPUT TYPE=HIDDEN NAME=ul VALUE=http://www.something.com/>
 - kategoryzacja witryny (doc/categories.txt)
 - moøliwe jest uruchomienie kilku procesÛw indeksuj±cych na kilku
   (teoretycznie 128) hostach i trzymanie bazy na jednym z nich,
   reindeksacja nie powoduje wtedy niedostÍpno∂ci wyszukiwarki.
   Przeczytaj cachemode.txt

W odrÛønieniu od innych systemÛw bazuj±cych na WAIS-ie lub serwerach
www, mnogosearch moøe ≥±czyÊ kilka serwerÛw www w jednym miejscu. Typ
serwera nie ma znaczenia, dopÛki pracuje on zgodnie z protoko≥em HTTP
1.0. Pakiet wspÛ≥pracuje rÛwnieø z domenami wirtualnymi.

%package devel
Summary:	Include files and libraries for mnogo
Summary(pl):	Pliki nag≥Ûwkowe dla mnogo
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
This package contains mnogosearch development files.

%description devel -l pl
Pliki dla programistÛw mnogosearch.

%if%{?_pgsql:1}%{!?_pgsql:0}

%package pgsql
Summary:	mnogosearch with pgsql storage-support 
Summary(pl):	mnogosearch z pgsqlem jako metod± przechowywania danych
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/NarzÍdzia
Group(pt_BR):	Rede/Utilit·rios
Requires:	%{name} = %{version}

%description pgsql
This package contains pgsql storage support.

Note: install will try to create tables in database mnogosearch.

%description pgsql -l pl
Ten pakiet zawiera wsparcie dla postgresa jako sposobu przechowywania
informacji. 

Instalacja tego pakietu spowoduje za≥oøenie tabel w bazie mnogosearch.
%endif

%package static
Summary:	mnogo static libraries
Summary(pl):	Biblioteki statyczne mnogo
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
This package contains static libraries of mnogosearch.

%description static -l pl
Ten pakiet zawiera statyczne biblioteki mnogosearch.

%prep
%setup -q
%patch0 -p0
#%patch1 -p0

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c

db="--with-built-in"

%{?_mysql: db="--with-mysql"}
%{?_pgsql: db="--with-pgsql"}

%configure \
	--enable-syslog      \
	--enable-syslog=LOG_LOCAL6 \
	--with-image-dir=/home/httpd/html/%{name} \
	--with-cgi-bin-dir=/home/httpd/cgi-bin \
	--with-search-dir=/home/httpd/html \
	--with-config-dir=%{_sysconfdir}/http/%{name} \
	--infodir=%{_infodir} \
	--with-openssl \
	$db \
	--enable-linux-pthreads \
	--enable-charset-guesser \
	--enable-news-extension \
	--enable-fast-tag \
	--enable-fast-cat \
	--enable-fast-site \
	--enable-phrase    \

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
install -d $RPM_BUILD_ROOT{/var/lib/mnogosearch,/etc/cron.daily,/home/httpd/html/%{name},%{_sysconfdir},%{_infodir}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

ln -sf ../..%{_sbindir}/indexer \
	$RPM_BUILD_ROOT/etc/cron.daily/mnogo-dbgen

ln -sf ../../../..%{_defaultdocdir}/%{name} \
        $RPM_BUILD_ROOT/home/httpd/html/%{name}/mnogodoc

install etc/search.htm-dist $RPM_BUILD_ROOT/home/httpd/html/search.html
install -d $RPM_BUILD_ROOT/home/httpd/cgi-bin

install $RPM_BUILD_ROOT%{_bindir}/search.cgi $RPM_BUILD_ROOT/home/httpd/cgi-bin/search.cgi
touch $RPM_BUILD_ROOT%{_sysconfdir}/locals
install %{SOURCE1} \
	$RPM_BUILD_ROOT/etc/cron.daily/mnogosearch-gethostnames
install %{SOURCE2} create/

gzip -z9 create/*
gzip -z9 create/*/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
cp -f %{_sysconfdir}/indexer.conf-dist %{_sysconfdir}/indexer.conf

cat << EOF
Please see docs (%{_defaultdocdir}/%{name} or http://localhost/mnogodoc), 
then read how to setup db connection, and put line like this 
"pgsql://user:password@/dbname/" into %{_sysconfdir}, then run sth like 
psql < %{_defaultdocdir}/%{name}/pgsql/*.txt
EOF


%if%{?_pgsql:1}%{!?_pgsql:0}

%post pgsql
echo 'Now I will try to Create Tables for postgres: '
su postgres -c "psql -U postgres template1 -c 'CREATE DATABASE mnogosearch;' "
echo "Trying to Create Tables:"
su postgres -c "psql -U postgres mnogosearch < /usr/share/doc/mnogosearch-3.1.17/pgsql/create.txt"
echo "Trying to Create Tables for crc-multi storage method:"
su postgres -c "psql -U postgres mnogosearch < /usr/share/doc/mnogosearch-3.1.17/pgsql/crc-multi.txt"
echo "Trying to Create Tables for news extension:"
su postgres -c "psql -U postgres mnogosearch < /usr/share/doc/mnogosearch-3.1.17/pgsql/news-extension.txt"
echo "Mnogosearch user will be created with passwd aqq123 change it ! and I mean it really !"
echo 'CREATE USER "mnogosearch" WITH PASSWORD '"'aqq123'"' NOCREATEDB NOCREATEUSER;' > /tmp/aqq
su postgres -c "psql -U postgres mnogosearch < /tmp/aqq"
echo "Granting Permisions..."
cat > /tmp/mnogo.aqq << EOF

GRANT ALL ON url,dict,robots,stopword,categories,next_url_id,affix TO mnogosearch;

GRANT ALL ON ndict,server,thread,spell,next_cat_id,next_server_id,next_url_id TO mnogosearch;

GRANT ALL ON ndict2,ndict3,ndict4,ndict5,ndict6,ndict7,ndict8,ndict9,
ndict10,ndict11,ndict12,ndict16,ndict32 TO mnogosearch;

GRANT ALL ON dict2,dict3,dict4,dict5,dict6,dict7,dict8,dict9,dict10,
dict11,dict12,dict16,dict32 TO mnogosearch;

GRANT ALL ON "qtrack" TO mnogosearch;
EOF
su postgres -c "psql -U postgres template1 -f /tmp/mnogo.aqq"
rm -f /tmp/mnogo.aqq

%postun pgsql
echo -n 'Dropping Database mnogosearch:' 
su postgres -c "psql -U postgres template1 -c 'DROP DATABASE mnogosearch;' "
%endif # _pgsql
	
%files
%defattr(644,root,root,755)
%doc COPYING README doc/* create/* create/*/*
#%doc %{_infodir}/*
%dir /var/lib/%{name}
%attr (755,http,http) /home/httpd/cgi-bin/*
%attr (755,http,http) %{_bindir}/*
%attr (755,http,http) %{_sbindir}/*
%attr (755,http,http) %{_libdir}/*
#%attr (755,http,http) %{_libdir}/%{name}/*la
%config(noreplace) /home/httpd/html/%{name}/*
#%{_datadir}/%{name}/*
%config(noreplace) %verify(not size mtime md5) /home/httpd/html/search.html
%config(noreplace) %{_sysconfdir}/*
%config(noreplace) %attr(750,http,http) /etc/cron.daily/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*

%files static
%defattr(644,root,root,755)
#%{_libdir}/%{name}/*.a
