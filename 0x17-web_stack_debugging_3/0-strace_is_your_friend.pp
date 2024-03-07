# This manifest fixes the Apache 500 error by setting file permissions

file { '/path/to/your/apache/config/file':
 ensure => 'file',
 mode   => '0644',
}
