import React from 'react';
import clsx from 'clsx';
import styles from './Footer.module.css';

type FooterLink = {
  title: string;
  href?: string;
  to?: string;
};

type FooterSection = {
  title: string;
  links: FooterLink[];
};

type FooterProps = {
  sections?: FooterSection[];
  copyright?: string;
  additionalInfo?: string;
};

const Footer = ({ 
  sections, 
  copyright = `Copyright © ${new Date().getFullYear()} Physical AI & Humanoid Robotics Book. Built with Docusaurus.`,
  additionalInfo 
}: FooterProps): JSX.Element => {
  return (
    <footer className={clsx('footer', styles.footer)}>
      <div className="container">
        {sections && sections.length > 0 && (
          <div className="row">
            {sections.map((section, index) => (
              <div key={index} className="col col--3">
                <h4>{section.title}</h4>
                <ul>
                  {section.links.map((link, linkIndex) => (
                    <li key={linkIndex}>
                      {link.to ? (
                        <a href={link.to}>{link.title}</a>
                      ) : (
                        <a href={link.href} target="_blank" rel="noopener noreferrer">
                          {link.title}
                        </a>
                      )}
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        )}
        <div className={styles.copyright}>
          <p>{copyright}</p>
          {additionalInfo && <p>{additionalInfo}</p>}
        </div>
      </div>
    </footer>
  );
};

export default Footer;