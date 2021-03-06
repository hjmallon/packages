# This is a meta package to require all of the individual firmware packages.

Summary:	Firmwares for the compat-wireless package
Name:		compat-wireless-firmware
Version:	3.5
Release:	1%{?dist}
License:	GPLv2
Group:		System Environment/Kernel
URL:		http://elrepo.org/

BuildArch: noarch

# Some firmwares are provided by kernel-firmware whereas others are provided by
# individual firmware packages. Lets pull them all in here plus any of our own

# Require the kernel-firmware package
Requires: kernel-firmware
# Require the individual firmware packages
Requires: ath9k_htc-firmware
Requires: bcm43xx-firmware
# Intel firmwares
# these are version dependant - we might need newer versions of these at some point
# or we might need to add new firmwares not in the distro
Requires: ipw2100-firmware
Requires: ipw2200-firmware
Requires: iwl100-firmware
Requires: iwl1000-firmware
Requires: iwl3945-firmware
Requires: iwl4965-firmware
Requires: iwl5000-firmware
Requires: iwl5150-firmware
Requires: iwl6000-firmware
Requires: iwl6050-firmware
Requires: iwl6000g2a-firmware
Requires: iwl6000g2b-firmware
# Marvell Libertas firmware
Requires: libertas-usb8388-firmware
# Ralink firmwares
Requires: rt61pci-firmware
Requires: rt73usb-firmware
Requires: rt2860-firmware
Requires: rt2870-firmware
# ZyDAS firmware
Requires: zd1211-firmware

%description
This package installs all of the individual firmware packages
required for the compat-wireless drivers package.

%prep
# nothing to prep

%build
# nothing to build

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)

%changelog
* Thu Aug 16 2012 Philip J Perry <phil@elrepo.org> - 3.5-1
- Add kernel-firmware
- Add bcm43xx-firmware

* Tue Jun 05 2012 Philip J Perry <phil@elrepo.org> - 3.3-2
- Add other firmwares

* Sat May 12 2012 Philip J Perry <phil@elrepo.org> - 3.3-1
- Initial package for compat-wireless firmwares
  [http://elrepo.org/bugs/view.php?id=273]
