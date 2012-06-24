Summary:	Tetris-like game extended by colors
Summary(es):	Juego tipo Tetris, mejorado con ayuda de colores
Summary(pl):	Tetriso-podobna gra rozszerzona o kolorki
Summary(pt_BR):	Jogo tipo Tetris, incrementado por cores, multin�vel
Name:		nct
Version:	1.4
Release:	2
License:	GPL
Group:		Applications/Games
Source0:	ftp://ftp.yars.free.net/pub/software/unix/games/tetris/%{name}-%{version}.tar.gz
# Source0-md5:	952a078ec2ecb05e0f19b50e0411837a
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
Requires(post):	fileutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tetris-like game, extended by colors. Light colors can be replaced by
heavy ones, playing various levels at the same time. Number of colors
can be chosen, in case of one color we get classic game.

%description -l es
Juego tipo Tetris, mejorado con ayuda de colores. Colores suaves
pueden reemplaz arse por colores m�s fuertes, as� se juega de manera
simult�nea con varios nivel es. Puede escogerse el n�mero de colores,
si se escoge s�lo uno, se tendr� el ju ego tetris cl�sico.

%description -l pl
Tetriso-podobna gra, rozszerzona o kolorki. Jasne kolorki mog� by�
zast�powane przez ciemne, mo�na gra� na r�nych poziomach w tym samym
czasie. Liczba kolork�w mo�e by� swobodnie dobierana, w przypadku
jednego koloru mamy do czynienia z klasycznym tetrisem.

%description -l pt_BR
Jogo tipo tetris, incrementado por cores. Cores leves podem ser
sobrepostas por cores mais pesadas, jogando-se com v�rios n�veis
simultaneamente. O n�mero de cores pode ser escolhido, e caso se
escolha apenas uma, se tem o Tetris cl�ssico.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_localstatedir}/games

%{__make} install DESTDIR=$RPM_BUILD_ROOT

touch	$RPM_BUILD_ROOT%{_localstatedir}/games/%{name}.score

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch %{_localstatedir}/games/%{name}.score
%{__chown} root.games %{_localstatedir}/games/%{name}.score
%{__chmod} 0664 %{_localstatedir}/games/%{name}.score

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(2755,root,games) %{_bindir}/%{name}
%attr(0664,root,games) %ghost %{_localstatedir}/games/%{name}.score
