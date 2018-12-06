# https://github.com/spacemonkeygo/spacelog
%global provider_prefix github.com/spacemonkeygo/spacelog
%global gobaseipath     %{provider_prefix}
%global commit          ae95ccc1eb0c8ce2496c43177430efd61930f7e4
%global commitdate      20150320

%gocraftmeta -i

Name:           %{goname}
Version:        0
Release:        0.10.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Hierarchical, leveled, and structured logging library for Go
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Patch1:         0001-Convert-dup2-calls-to-dup3.patch

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/spacemonkeygo/flagfile/utils)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gobaseipath} prefix.

%prep
%gosetup
%patch1 -p1 -b .dup2

%install
%goinstall

%check
%gochecks

%{!?_licensedir:%global license %%doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Mon Feb 26 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.20150320gitae95ccc
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitae95ccc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitae95ccc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitae95ccc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitae95ccc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.gitae95ccc
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sat Feb 27 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0-0.4.gitae95ccc
- Cleanup arch and license defs
- Fix syscall.Dup2 on aarch64

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.gitae95ccc
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitae95ccc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.gitae95ccc
- Update spec file to spec-2.0
  resolves: #1250513

* Mon Jun 15 2015 Marek Skalicky <mskalick@redhat.com> - 0-0.1.gitae95ccc
- First package for Fedora
  resolves: #1232231

