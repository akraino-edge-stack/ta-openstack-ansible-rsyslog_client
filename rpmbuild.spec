# Copyright 2019 Nokia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

Name:           openstack-ansible-rsyslog_client
Version:        17.0.2
Release:        1%{?dist}.1
License:        %{_platform_licence} and ASL 2.0
Source0:        https://github.com/openstack/%{name}/archive/%{version}.tar.gz
Patch0:         0001-initial.patch
Vendor:         %{_platform_vendor} and OpenStack modified
URL:            https://github.com/openstack/openstack-ansible-rsyslog_client
BuildArch:      noarch
Summary:        openstack-ansible-rsyslog_client
Requires:       openstack-ansible

%description
openstack-ansible-rsyslog_client

%prep
%autosetup -n %{name}-%{version} -p 1

%build

%install
mkdir -p %{buildroot}/etc/ansible/roles/rsyslog_client
rsync -av --exclude LICENSE --exclude rpmbuild.spec --exclude .git --exclude .gitreview . %{buildroot}/etc/ansible/roles/rsyslog_client/

%files
/etc/ansible/roles/rsyslog_client

