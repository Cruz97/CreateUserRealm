const App = {
    name: 'App',
    primaryKey: 'uuid',
    properties: {
        uuid: 'string?',
        name: 'string?'
        //contents: 'Content[]'
  
    }
  }
  
  const Menu = {
    name: 'Menu',
    primaryKey: 'uuid',
    properties: {
        uuid: 'string?',
        app: 'App?',
        actionsMenu : 'ActionsMenu[]'
    }
  }
  
  const Actions = {
    name: 'Actions', //screens   => details//home//
    primaryKey: 'uuid',
    properties: {
        uuid: 'string?',
        app: 'App?',
        name: 'string?',
        // isItemMenu: 'bool?'
    }
  }
  
  const Sections = {
    name: 'Sections', //secciones
    primaryKey: 'uuid',
    properties: {
        uuid: 'string?',
        sequence: 'int?', //priority order for show in a screen of menu
        limit: 'int?', //limit of items for show in screen  0 => all / n>0 => limit
        name: 'string?',
        
    }
  }
  
  
  const Content = {
    name: 'Content',  //Storage all content for a single App
    primaryKey: 'uuid',
    properties: {
        uuid: 'string?',
        app: 'App?',
        typeContent: 'TypeContent?',
        section: 'Sections?', // if is null, does not belong to any section
        name: 'string?',
        title: 'string?',
        subtitle: 'string?',
        date: 'date?',
        image: 'string?',
        summary: 'string?',
        create_at: 'date?',
        date_expire: 'date?'
    }
  }
  
  const TypeContent = {
    name: 'TypeContent',  //tickets//certificates//news//events//
    primaryKey: 'uuid',
    properties: {
        uuid: 'string?',
        app: 'App?',
        name: 'string?',
        action: 'Actions?',
        isItemMenu: 'bool?',
  
  
    }
  }
  
  const ActionsMenu = {
    name: 'ActionsMenu',
    primaryKey: 'uuid',
    properties: {
        uuid: 'string?',
        // app: 'App?',
        name: 'string?',
        icon: 'string?',
        sections: 'Sections[]', //show many sections in a screen //if is null show a Action,
        icon_type: 'string?'
    }
  }
  
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
      organizator: 'string?'
  
    }
  }
  
  
module.exports = [
    App,
    Menu,
    Actions,
    Sections,
    Content,
    TypeContent,
    ActionsMenu
  ];
  