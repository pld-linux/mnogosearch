Summary:	A another one web indexing and searching system for a small domain or intranet
Summary(pl):	Kolejny System indeksowania i przeszukiwania www dla ma�ych domen i intranetu
Name:		mnogosearch
Version:	3.1.17
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narz�dzia
Source0:	http://www.mnogosearch.ru/Download/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Source1:	%{name}-gethostnames
URL:		http://www.mnogosearch.ru/
BuildRequires:	postgresql-devel
PreReq:		webserver
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
 - limiting queries to one hostname by sth like this: <INPUT TYPE=HIDDEN NAME=ul VALUE=http://www.something.com/>
 - it's posilble to run indexers on several diffrent (theoreticaly 128) hosts, and gather information on one of them, reindexing proceses make no harm to avalibility of search engine. See  cachemode.txt
 

As opposed to some WAIS-based or web-server based search engines,
mnogsearch can span several web servers at a site. The type of these
different web servers doesn't matter as long as they understand the
HTTP 1.0 protocol. Mnogosearch supports also virtual domains.

%description -l pl
Mnogosearch jest kompletnym systemem indeksuj�cym i przeszukuj�cym www
dla ma�ych domen oraz intranetu. System nie zosta� opracowany jako
wielki system typu Lycos, Infoseek WebCrawler i AltaVista. Natomiast
nadeje si� do zastosowania w pojedy�czej firmie, kampusie lub
jakiejkolwiek stronie www.
Zalety:
 - przeszukiwaie tagow mp3,
 - nius�w (Server news://localhost/pl/),
 - htdb czyli baz danych udost�pnianych przez www/cgi. (HTDBList SELECT concat("http://search.mnogo.ru/board/message.php?id=",id) \ FROM udm.messages LIMIT 2)) 
 - zawarto�ci serwer�w ftp (rada za 2gr "Index  no" dla serwera ftp spowoduje nie indexowanie *zawarto�ci* plik�w na nim si� znajduj�cych)
 - wyszykiwanie w zwyk�ych URLach http:// 
 - wsparcie dla ssl (https://)
 - wyszukiwanie w mirrorach [r�wnie� lokalnych] odleg�ych sieci
 - zgadywanie zestawu znakow
 - zewnetrzne przetwarzacze dokumentow na potrzeby indekosowania
 - ograniczanie zapyta� do jednej nazwy hosta:  <INPUT TYPE=HIDDEN NAME=ul VALUE=http://www.something.com/>
 - kategoryzacja witryny (doc/categories.txt)
 - mo�liwe jest uruchomienie kilku proces�w indeksuj�cych na kilku (teoretycznie 128) hostach i trzymanie bazy na jednym z nich, reindeksacja nie powoduje wtedy niedost�pno�ci wyszukiwarki. Przeczytaj cachemode.txt

W odr�nieniu od innych system�w bazuj�cych na WAIS-sie lub serwerch www,
mnogosearch mo�e ��czy� kilka serwer�w www w jednym miejscu. Typ serwera 
nie ma znaczenia, dop�ki pracuje on zgodnie z protoko�em HTTP 1.0. Pakiet
wsp�pracuje r�wnie� z domenami wirtualnymi.

%package devel
Summary:	Include files and libraries for mnogo
Summary(pl):	Pliki nag��wkowe dla mnogo
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The mnogosearch system is a complete world wide web indexing and
searching system for a small domain or intranet. This system is not
meant to replace the need for powerful internet-wide search systems
like Lycos, Infoseek, Webcrawler and AltaVista. Instead it is meant to
cover the search needs for a single company, campus, or even a
particular sub section of a web site.

As opposed to some WAIS-based or web-server based search engines,
mnogosearch can span several web servers at a site. The type of these
different web servers doesn't matter as long as they understand the
HTTP 1.0 protocol. Mnogosearch supports also virtual domains.

This package contains devlopment files.

%package pgsql
Summary:	mnogosearch w/ pgsql storage-support 
Summary(pl):	mnogosearch z pgsqlem jako metod� przechowywania danych
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narz�dzia
Requires:	%{name} = %{version}

%description pgsql
The mnogosearch system is a complete world wide web indexing and
searching system for a small domain or intranet. This system is not
meant to replace the need for powerful internet-wide search systems
like Lycos, Infoseek, Webcrawler and AltaVista. Instead it is meant to
cover the search needs for a single company, campus, or even a
particular sub section of a web site.

As opposed to some WAIS-based or web-server based search engines,
mnogosearch can span several web servers at a site. The type of these
different web servers doesn't matter as long as they understand the
HTTP 1.0 protocol. Mnogosearch supports also virtual domains.

This package contains pgsql storage support.

%package static
Summary:	mnogo static libraries
Summary(pl):	Biblioteki statyczne mnogo
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
The mnogosearch system is a complete world wide web indexing and
searching system for a small domain or intranet. This system is not
meant to replace the need for powerful internet-wide search systems
like Lycos, Infoseek, Webcrawler and AltaVista. Instead it is meant to
cover the search needs for a single company, campus, or even a
particular sub section of a web site. As opposed to some WAIS-based or
web-server based search engines, mnogosearch can span several web servers
at a site. The type of these different web servers doesn't matter as
long as they understand the HTTP 1.0 protocol. Mnogosearch supports also 
virtual domains. This package contains static libraries of mnogosearch.

%prep
%setup -q
%patch0 -p1

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c
#where the hell is pgsql?
sed -e 's/usr\/include\/pgsql/usr\/include\/postgresql/' < configure.in > aqq
mv aqq  configure.in
%configure \
	--enable-syslog      \
	--enable-syslog=LOG_LOCAL6 \
	--with-image-dir=/home/httpd/html/%{name} \
	--with-cgi-bin-dir=/home/httpd/cgi-bin \
	--with-search-dir=/home/httpd/html \
	--with-config-dir=%{_sysconfdir}/http/%{name} \
	--infodir=%{_infodir} \
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

gzip -z9 create/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
cp %{_sysconfdir}/indexer.conf-dist %{_sysconfdir}/indexer.conf


cat << EOF
Please see docs (%{_defaultdocdir}/%{name} or http://localhost/mnogodoc), 
then read how to setup db connection, and put line like this 
"pgsql://user:password@/dbname/" into %{_sysconfdir}, then run sth like 
psql < %{_defaultdocdir}/%{name}/pgsql/*.txt
Now I will try to Create Tables for postgres: 
EOF
su postgres -c "psql -U postgres template1 -c 'CREATE DATABASE mnogosearch;' "
echo "Trying to Create Tables:"
su postgres -c "psql -U postgres mnogosearch < /usr/share/doc/mnogosearch-3.1.17/pgsql/create.txt"
echo "Trying to Create Tables for crc-multi storage method:"
su postgres -c "psql -U postgres mnogosearch < /usr/share/doc/mnogosearch-3.1.17/pgsql/crc-multi.txt"
echo "Trying to Create Tables for news extension:"
su postgres -c "psql -U postgres mnogosearch < /usr/share/doc/mnogosearch-3.1.17/pgsql/news-extension.txt"
echo "Mnogosearch user will be created with passwd aqq123 change it ! and I mean it realy !"
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
#%{_includedir}/%{name}/*

%files static
%defattr(644,root,root,755)
#%{_libdir}/%{name}/*.a
