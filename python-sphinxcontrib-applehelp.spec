%define	module	sphinxcontrib-applehelp

Summary:	Apple help file support for the Sphinx documentation generator
Name:		python-%{module}
Version:	2.0.0
Release:	1
Source0:	https://github.com/sphinx-doc/%{module}/archive/%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		http://sphinx-doc.org/
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildSystem:	python
# Not really, but let's get rid of py2 cruft
Obsoletes:	python2-%{module} < %{EVRD}

%description
Web support for the Sphinx documentation generator

%files
%{py_puresitedir}/sphinxcontrib*
