#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	httpx_sse
Summary:	Consume Server-Sent Event (SSE) messages with HTTPX
Summary(pl.UTF-8):	Obsługa komunikatów Server-Sent Event (SSE) z HTTPX
Name:		python3-httpx-sse
Version:	0.4.3
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/httpx-sse/
Source0:	https://files.pythonhosted.org/packages/source/h/httpx-sse/%{module}-%{version}.tar.gz
# Source0-md5:	ec38c44149578e3b519a12c1b75b3558
URL:		https://github.com/florimondmanca/httpx-sse
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-httpx >= 0.27.1
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Consume Server-Sent Event (SSE) messages with HTTPX.

%description -l pl.UTF-8
Biblioteka do obsługi komunikatów Server-Sent Event (SSE) z użyciem
HTTPX.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md CHANGELOG.md
%{py3_sitescriptdir}/httpx_sse
%{py3_sitescriptdir}/httpx_sse-%{version}.dist-info
