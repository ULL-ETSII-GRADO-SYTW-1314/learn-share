require 'dm-core'  
require 'dm-timestamps'  
require 'dm-validations'  
require 'dm-migration'

class Task  
    include DataMapper::Resource  
      
    property :id       , Serial  
    property :assessment , Float
end 