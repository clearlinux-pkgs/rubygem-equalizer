#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-equalizer
Version  : 0.0.11
Release  : 4
URL      : https://rubygems.org/downloads/equalizer-0.0.11.gem
Source0  : https://rubygems.org/downloads/equalizer-0.0.11.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support

%description
equalizer
=========
Module to define equality, equivalence and inspection methods

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n equalizer-0.0.11
gem spec %{SOURCE0} -l --ruby > rubygem-equalizer.gemspec

%build
gem build rubygem-equalizer.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
equalizer-0.0.11.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/equalizer-0.0.11
rspec -I.:lib spec/
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/equalizer-0.0.11.gem
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/.rubocop.yml
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/.ruby-gemset
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/.ruby-version
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/.yardstick.yml
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/README.md
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/config/devtools.yml
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/config/flay.yml
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/config/flog.yml
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/config/mutant.yml
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/config/reek.yml
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/config/rubocop.yml
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/config/yardstick.yml
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/equalizer.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/lib/equalizer.rb
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/lib/equalizer/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/spec/support/config_alias.rb
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/spec/unit/equalizer/included_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/spec/unit/equalizer/methods/eql_predicate_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/spec/unit/equalizer/methods/equality_operator_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/equalizer-0.0.11/spec/unit/equalizer/universal_spec.rb
/usr/lib64/ruby/gems/2.3.0/specifications/equalizer-0.0.11.gemspec
