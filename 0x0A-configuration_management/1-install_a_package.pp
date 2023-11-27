# Using puppet to install flask from pip3
package { 'flask==2.1.0':
ensure   => link,
provider => 'pip3'
}
