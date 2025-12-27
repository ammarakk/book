import React from 'react';
import Layout from '@theme/Layout';
import { TranslationToggle, TranslatedContent } from '../components';
import { useAuth } from '../contexts/AuthContext';

function DocPage(props) {
  const { content: DocContent } = props;
  const { metadata } = DocContent;
  const { is_authenticated } = useAuth(); // Assuming this context provides auth state

  return (
    <Layout
      title={`${metadata.title}`}
      description={metadata.description}>
      <div className="container margin-vert--lg">
        <div className="row">
          <main className="col col--8 col--offset-2">
            {/* Show the translation button only if the user is authenticated */}
            {is_authenticated && (
              <TranslationToggle chapterId={metadata.unversionedId} />
            )}
            
            <header className="postHeader">
              <h1>{metadata.title}</h1>
            </header>
            
            <article>
              <DocContent />
              
              {/* Show translated content if available */}
              <TranslatedContent chapterId={metadata.unversionedId} />
            </article>
          </main>
        </div>
      </div>
    </Layout>
  );
}

export default DocPage;