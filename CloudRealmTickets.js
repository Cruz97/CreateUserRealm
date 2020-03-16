const Tickets = {
    name: 'Tickets',
    primaryKey: 'uuid',
    properties: {
      uuid: 'string?',
      name_user: 'string?',
      entry: 'string?',
      event: 'string?',
      date: 'string?',
      address: 'string?',
      order_number: 'int?',
      event_summary: 'string?',
      organizator: 'string?',
      date_event: 'date?',
      image: 'string?'
  
    }
  }
  

module.exports = [
    Tickets
  ];