# Change the OS configuration

# Increase hard file limit
exec {
  command => "sed -i '/holberton hard/s/5/4096/' /etc/security/limits.conf",
  path    => "/usr/local/bin/:/bin"
}

# Increase soft file limit
exec { 'increase-soft-file-limit-for-holberton-user':
  command => "sed -i '/holberton soft/s/4/4096/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}
