require 'dm-core'  
require 'dm-timestamps'  
require 'dm-validations'  
require 'dm-migration'

class User  
    include DataMapper::Resource  
      
    property :id       , Serial  
    property :username , String
    property :name , String
    property :password , String
    property :email    , String, format: :email_address
    property :points , Integer
    property :assessment , Float
    property :country    , String
end 